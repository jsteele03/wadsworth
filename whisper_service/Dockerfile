FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y ffmpeg && \
    pip install faster-whisper sounddevice numpy scipy

CMD ["python3", "main.py"]
