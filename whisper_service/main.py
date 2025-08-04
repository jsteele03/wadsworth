# from faster_whisper import WhisperModel
# model = WhisperModel("small", device="cpu", compute_type="int8")

# segments, info = model.transcribe("../data/audio/Recording.mp3", beam_size=5)

# for segment in segments:
#     print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

# ============================================================================ #

# import nemo.collections.asr as nemo_asr

# asr_model = nemo_asr.models.EncDecCTCModelBPE.from_pretrained(
#     model_name="nvidia/parakeet-ctc-0.6b"
# )

# transcript = asr_model.transcribe(['../data/audio/Recording.mp3'])
# print(transcript)

# ============================================================================ #

# import sounddevice as sd
# import numpy as np
# import scipy.io.wavfile
# import os
# import time
# from faster_whisper import WhisperModel

# MODEL_NAME = "tiny"  # smaller and faster, adjust if you want
# SAMPLE_RATE = 16000
# CHANNELS = 1
# RECORD_SECONDS = 5
# AUDIO_DIR = "./audio"

# os.makedirs(AUDIO_DIR, exist_ok=True)

# model = WhisperModel(MODEL_NAME, device="cpu", compute_type="int8")

# def record_audio(filename):
#     print("Recording audio...")
#     audio = sd.rec(int(SAMPLE_RATE * RECORD_SECONDS), samplerate=SAMPLE_RATE, channels=CHANNELS)
#     sd.wait()
#     scipy.io.wavfile.write(filename, SAMPLE_RATE, audio)
#     print(f"Saved recording to {filename}")

# def transcribe_audio(filename):
#     print(f"Transcribing {filename} ...")
#     segments, _ = model.transcribe(filename)
#     text = " ".join([segment.text for segment in segments]).lower()
#     print(f"Transcription: {text}")
#     return text

# def main_loop():
#     count = 0
#     while True:
#         filename = os.path.join(AUDIO_DIR, f"recording_{count}.wav")
#         record_audio(filename)
#         transcript = transcribe_audio(filename)
        
#         if "mr. wadsworth" in transcript:
#             print("Went into main protocol")
#             # Here you can trigger further logic or break the loop
#         else:
#             print("Phrase not detected. Deleting file.")
#             os.remove(filename)
        
#         count += 1
#         time.sleep(0.5)  # slight delay before next recording

# if __name__ == "__main__":
#     main_loop()


# main.py
import sys
import os
from faster_whisper import WhisperModel

TRIGGER_PHRASE = "this dream is real"

filename = sys.argv[1] if len(sys.argv) > 1 else "../data/audio/clip.wav"

model = WhisperModel("small", device="cpu", compute_type="int8")
segments, _ = model.transcribe(filename, beam_size=5)

transcript = " ".join(segment.text for segment in segments).lower()
print("Transcript:", transcript)

if TRIGGER_PHRASE in transcript:
    print("Went into main protocol.")
else:
    print("Trigger phrase not found.")

