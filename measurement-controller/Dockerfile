FROM python:3.10-slim

WORKDIR /app
RUN pip install matplotlib
COPY controller.py .
COPY plot_utils.py .

CMD ["python3", "controller.py"]
