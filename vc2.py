import speech_recognition as sr
import os
from gtts import gTTS
import time

def speak(audio):
    print(audio)
    gt=gTTS(text=audio,lang='en')
    gt.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def record():
    r=sr.Recognizer()
    with sr.Microphone(sample_rate=48000) as source:
        print("Say!")
        r.adjust_for_ambient_noise(source,duration=5)
        audio=r.listen(source)

        data=""
        try:
            data=r.recognize_google(audio)
            speak(audio)
        except sr.UnknownValueError:
            print("Command not recognized")
        except sr.RequestError as e:
            print("Could not request result".format(e))
    return  data

def alfareeda(data):
    if "how are you?" in data:
        speak("I am fine")
    elif "who am I?" in data:
        speak("whiteknight")
    elif "what time is it" in data:
        os.system("date")
time.sleep(2)
speak("Hello! I am alfareeda")
while 1:
    data=record()
    alfareeda(data)