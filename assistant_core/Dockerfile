FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install openai faster-whisper TTS numpy sounddevice \
    langchain chromadb flask requests

CMD ["python3", "assistant.py"]
