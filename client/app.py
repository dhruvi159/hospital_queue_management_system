import time
import grpc
import json
import stomp
import os
import pybreaker

# gRPC stub (generated during image build)
import queue_pb2
import queue_pb2_grpc

# Circuit breaker: trips after 3 consecutive failures, resets after 30 seconds
grpc_breaker = pybreaker.CircuitBreaker(
    fail_max=3,
    reset_timeout=30,
    name="gRPC-Server"
)

@grpc_breaker
def call_grpc_queue():
	channel = grpc.insecure_channel('server:50051')
	stub = queue_pb2_grpc.QueueServiceStub(channel)
	resp = stub.GetQueue(queue_pb2.Empty())
	print('gRPC Queue:', resp.patients_waiting)
	for a in resp.appointments:
		print('-', a.patient_name, a.appointment_time)


class StompListener(stomp.ConnectionListener):
	def on_message(self, headers, message):
		print('STOMP message received:', message)


def start_stomp_listener():
	conn = stomp.Connection([('activemq', 61613)])
	conn.set_listener('', StompListener())
	conn.start()
	conn.connect(wait=True)
	# subscribe to the queue used by server
	conn.subscribe(destination='/queue/hospital_queue', id=1, ack='client')
	return conn


if __name__ == '__main__':
	# call gRPC API with circuit breaker protection
	try:
		call_grpc_queue()
	except pybreaker.CircuitBreakerError:
		print('[CIRCUIT BREAKER] gRPC server is unavailable - circuit is OPEN, skipping request.')
	except Exception as e:
		print(f'[CIRCUIT BREAKER] gRPC call failed ({grpc_breaker.fail_counter}/3 failures): {e}')

	# Start STOMP listener only when explicitly enabled via env var
	start_listener = os.environ.get('START_STOMP_LISTENER', 'false').lower() == 'true'
	if not start_listener:
		print('STOMP listener disabled (set START_STOMP_LISTENER=true to enable)')
	else:
		try:
			conn = start_stomp_listener()
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			try:
				conn.disconnect()
			except Exception:
				pass
