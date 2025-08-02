FROM ubuntu:22.04

RUN apt-get update && apt-get install -y iperf3

RUN echo "Iperf3 is ready to run."