FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y ffmpeg && \
    pip install TTS sounddevice numpy

CMD ["python3", "speak.py"]