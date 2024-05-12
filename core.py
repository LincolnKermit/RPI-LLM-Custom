import os, openai, pyaudio
import speech_recognition as sr

openai_key = "none"

# MAC OS : brew install portaudio
# Ubuntu : sudo apt-get install python-pyaudio python3-pyaudio

# Global
# pip install pyaudio



r = sr.Recognizer()

print(sr.Microphone.list_microphone_names())


micro = sr.Microphone()


with micro as source:
    print("Speak!")
    audio_data = r.listen(source)
    print("End!")
result = r.recognize_google(audio_data)
print (">", result)

# pip install openai

# More coming...

