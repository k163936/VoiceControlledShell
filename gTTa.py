#!/usr/bin/env python3

from gtts import gTTS
import speech_recognition as sr
from time import ctime
import time
import os
def speak(audio):
    tts=gTTS(text=audio,lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")
def record():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say!!")
        audio=r.listen(source)
        data=""
        try:
            data=r.recognize_google(audio)
            print("You said"+data)
        except sr.UnknownValueError:
            print("Unkown value error")
        except sr.RequestError:
            print("Request error")
    return data
def alfred(data):
    if "hello alfred" in data:
        speak("Hello white knight")

time.sleep(2)
speak("Hello white knight what can I do for you")
while 1:
    data=record()
    alfred(data)