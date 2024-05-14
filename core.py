from gtts import gTTS
import os, openai, pyaudio, torch
import speech_recognition as sr


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
        tts = gTTS('Hello, I am your personnal assistant. How can I help you?')
        print("Speak!")
        audio_data = r.listen(source)
        print("End!")
    result = r.recognize_google(audio_data)
    print (">", result)
    tts = gTTS('Have you said, "' + result + '"?')
    while result != "yes" or result != "exactly" or result != "True" or result != "of course":
        with micro as source:
            tts = gTTS('I am sorry that I am not able to understand you. Can you please repeat?')
            print("Speak!")
            audio_data = r.listen(source)
            print("End!")
        result = r.recognize_google(audio_data)



# pip install openai

# More coming...
