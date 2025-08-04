# FROM python:3.10-slim

# WORKDIR /app
# COPY . /app

# RUN apt-get update && apt-get install -y ffmpeg && \
#     pip install faster-whisper sounddevice numpy scipy

# CMD ["python3", "main.py"]

FROM python:3.10-slim

WORKDIR /app
COPY . /app

# Install dependencies: ffmpeg for Whisper, libportaudio2 for sounddevice, and alsa-utils for audio
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libportaudio2 \
    libsndfile1 \
    alsa-utils \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir faster-whisper sounddevice numpy scipy

CMD ["python3", "main.py"]
