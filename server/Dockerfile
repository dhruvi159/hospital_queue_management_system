FROM python:3.11-alpine

WORKDIR /app

COPY server/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy proto files and generate gRPC stubs during build
COPY proto ./proto
RUN python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/queue.proto || true

# Copy only server sources into image (build context is repo root)
COPY server/ .

CMD ["python", "main.py"]
