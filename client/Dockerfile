FROM python:3.11-alpine

WORKDIR /app
RUN pip install requests grpcio grpcio-tools protobuf stomp.py pybreaker

# Copy proto and generate client stubs
COPY proto ./proto
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/queue.proto || true

# Copy only client sources into image (build context is repo root)
COPY client/ .

CMD ["python", "app.py"]
