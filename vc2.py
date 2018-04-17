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
        except sr.UnknownValueError:
            print("Command not recognized")
        except sr.RequestError as e:
            print("Could not request result".format(e))

    return str(data).lower()

def alfareeda(data):
    if "how are you" in data:
        speak("I am fine")
    elif "who am i" in data:
        speak("whiteknight")
    elif "what time is it" in data:
        os.system("date")
    elif "list files" in data:
        os.system("ls")
    elif "list all files" in data:
        os.system("ls -a")
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
        if "to home" in data:
            os.system("cd ..")
        else:
            speak("tell me the name of the directory")
            dir=record()
            dir.replace(" ","")
            os.system("cd "+dir)
    elif "copy file" in data:
        speak("tell source")
        s=record()
        speak("tell the type of file")
        t=record()
        t.replace(" ","")
        s=s+"."+t
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
    elif "exit" in data:
        os.system("quit()")
    elif "clear" in data:
        os.system("clear")
    elif "find all text files" in data:
        os.system("find *.txt")
    elif "create text file" in data:
        speak("tell the name of file")
        t=record()
        t=t+".txt"
        os.system("touch "+t)
    elif "create directory" in data:
        speak("tell the name of the directory")
        t=record()
        os.system("mkdir "+t)
    elif "remove file" in data:
        speak("tell the name of file")
        n=record()
        n.replace(" ","")
        speak("tell the type of file")
        t=record()
        c=n+"."+t
        os.system("rm "+c)
    elif "remove folder" in data:
        speak("enter the name of the folder")
        n=record()
        n.replace(" ","")
        os.system("rmdir "+n)
    elif "shutdown" in data:
        os.system("shutdown now")
    elif "restart" in data:
        os.system("shutdown -f now")
    elif "head" in data:
        speak("tell the name of file")
        n=record()
        n.replace(" ","")
        speak("tell the type of file")
        t=record()
        t.replace(" ","")
        c=n+"."+t
        os.system("head "+c)
    elif "tail" in data:
        speak("tell the name of file")
        n = record()
        n.replace(" ", "")
        speak("tell the type of file")
        t = record()
        t.replace(" ", "")
        c = n + "." + t
        os.system("tail " + c)
    elif "current direcctory" in data:
        os.system("pwd")
    elif "network status" in data:
        os.system("ifconfig -a")
    elif "running processes" in data:
        os.system("ps")
    elif "all processes" in data:
        os.system("ps -A")
    elif  "details of disk" in data:
        os.system("df")
    elif "details of file usage" in data:
        os.system("du")
    elif "login as root user" in data:
        os.system("sudo -i")



time.sleep(2)
speak("Hello! I am alfareeda")
while 1:
    data=record()
    alfareeda(data)
