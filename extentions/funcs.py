import os

import playsound
import speech_recognition as sr
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    voice = "voice.mp3"
    tts.save(voice)
    playsound.playsound(voice)
    os.remove(voice)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except:
            pass

    return said