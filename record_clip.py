import sounddevice as sd
import scipy.io.wavfile
import os

os.makedirs("audio", exist_ok=True)

samplerate = 16000
duration = 5
filename = "audio/clip.wav"

print("Recording...")
recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
sd.wait()
scipy.io.wavfile.write(filename, samplerate, recording)
print("Saved:", filename)

# ============== working version that runs container ============== #

# import subprocess
# import sounddevice as sd
# import scipy.io.wavfile
# import os

# AUDIO_DIR = "audio"
# FILENAME = "clip.wav"
# SAMPLERATE = 16000
# DURATION = 5
# AUDIO_PATH = os.path.join(AUDIO_DIR, FILENAME)

# # 1. Record audio on host
# os.makedirs(AUDIO_DIR, exist_ok=True)
# print("Recording...")
# recording = sd.rec(int(DURATION * SAMPLERATE), samplerate=SAMPLERATE, channels=1, dtype='int16')
# sd.wait()
# scipy.io.wavfile.write(AUDIO_PATH, SAMPLERATE, recording)
# print(f"Audio saved to: {AUDIO_PATH}")

# # 2. Run Docker Whisper container to transcribe it
# print("Transcribing with Whisper...")
# try:
#     subprocess.run(["docker", "compose", "up", "whisper"], check=True)
# except subprocess.CalledProcessError as e:
#     print("Error running transcription container:", e)

# # 3. TODO: clean up (delete the audio if no trigger found)
