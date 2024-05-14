from TTS.api import TTS
import os, openai, pyaudio, torch
import speech_recognition as sr
# pip3 install pyttsx3 - for text to speech - Recommanded version pip3
# Windows users might need to install "win32api"






print("Initalising TTSCore...")
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
# Model is approxitaely 2GB in size, so it might take some time to load...
# 130 MB in lib folder, 1.8 GB in models folder







# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
wav = tts.tts(text="Hello world!", speaker_wav="my/cloning/audio.wav", language="en")




openai_key = "none"

# MAC OS : brew install portaudio
# Ubuntu : sudo apt-get install python-pyaudio python3-pyaudio

# Global
# pip install pyaudio


print("Initializing Speech Recognition...")
r = sr.Recognizer()
print("Fetching microphone names...")
print(sr.Microphone.list_microphone_names())


print("Initializing Microphone...")
micro = sr.Microphone()

print("End of setup, ready to listen!")

while True:
    with micro as source:
        print("Speak!")
        audio_data = r.listen(source)
        print("End!")
    result = r.recognize_google(audio_data)
    print (">", result)


# pip install openai

# More coming...
