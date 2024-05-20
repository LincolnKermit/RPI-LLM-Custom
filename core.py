from openai import OpenAI


from gtts import gTTS
import os, pyaudio, torch, io, pygame
import speech_recognition as sr
import uuid

# Incase openai is not updated...
os.system("openai migrate")

openai_key = "API_KEY_HERE"

# Initialize pygame mixer for audio playback
pygame.mixer.init()
os.system("clear")


client = OpenAI(api_key=openai_key)

# Initializing Speech Recognition
r = sr.Recognizer()

# Initializing Microphone
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # Adjust for ambient noise once at the start

print("End of setup, ready to listen!")

conversations = {}

def play_tts(text):
    tts = gTTS(text)
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    pygame.mixer.music.load(fp, 'mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass

def get_chat_response(user_input, chat_id):
    global conversations
    prompt = conversations.get(chat_id, "") + "\n" + user_input
    response = client.completions.create(
        model="gpt-3.5-turbo-0125",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text.strip()
    conversations[chat_id] = conversations.get(chat_id, "") + "\nHuman: " + user_input + "\nAI: " + answer
    return answer


while True:
    play_tts('Hello, I am your personal assistant. How can I help you?')

    with sr.Microphone() as source:
        print("Speak!")
        audio_data = r.listen(source)
        print("End!")

    try:
        result = r.recognize_google(audio_data, language='en-US')
        print(f"You said: {result}")
        if "exit" in result.lower():
            break

        # Generate a unique chat ID if it's a new conversation
        chat_id = str(uuid.uuid4())
        response_text = get_chat_response(result, chat_id)
        play_tts(response_text)
        print(response_text)

    except sr.UnknownValueError:
        play_tts("Sorry, I did not catch that. Could you please repeat?")

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

