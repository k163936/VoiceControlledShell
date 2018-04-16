from gtts import gTTS
import speech_recognition as sr
import os
import time
def speak(audio):
    print(audio)
    gt=gTTS(text=audio,lang='en')
    gt.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())

        data = ""
        try:
            data = r.recognize_google(audio)
            print(data)
            return str(data).lower()
        except sr.UnknownValueError:
            print("Command not recognized")
            return None
        except sr.RequestError as e:
            print("Could not request result".format(e))
            return None

def alfareeda(data):
    if "how are you" in data:
        speak("I am fine")
    elif "who am i" in data:
        speak("whiteknight")
    elif "what time is it" in data:
        os.system("date")
    elif "list all files" in data:
        os.system("ls")
    elif "move file" in data:
        speak("tell source")
        s=record()
        speak("tell the type of file")
        t=record()
        t.replace(" ","")
        s=s+t
        speak("tell destination")
        d=record()
        os.system("mv "+s+" "+d)
    elif "change directory" in data:
        speak("tell me the name of the directory")
        dir=record()
        dir.replace(" ","")
        os.system("cd "+dir)
    elif "change directory to home" in data:
        os.system("cd .." )
    elif "copy file" in data:
        speak("tell source")
        s=record()
        speak("tell the type of file")
        t=record()
        t.replace(" ","")
        s=s+t
        speak("tell destination")
        d=record()
        os.system("cp "+s+" "+d)
    elif "copy folder" in data:
        speak("tell source")
        s=record()
        speak("tell the type of file")
        t=record()
        t.replace(" ","")
        s=s+t
        speak("tell destination")
        d=record()
        os.system("cp -r "+s+" "+d)
    elif "what is the kernel version" in data:
        os.system("uname -r")

time.sleep(2)
speak("Hello! I am alfareeda")
while 1:
    data=record()
    alfareeda(data)
