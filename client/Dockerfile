FROM python:3.10-slim

RUN apt-get update && apt-get install -y iperf3 netcat-openbsd

WORKDIR /app
COPY . .

CMD ["python3", "run_iperf_test.py"]