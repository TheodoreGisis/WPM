# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app

COPY app.py .

CMD ["python3","app.py"]
