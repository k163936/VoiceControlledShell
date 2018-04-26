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
        print("Say some valid command!")
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
def show_ext():
    ext = ["txt", "mp3", "mp4", "png", "wav", "sh", "docx"]
    for i in range(0,len(ext)):
        print("%d:"+ext[i]+"\n",i)
    speak("select extension")
    d=record()
    d=int(d)
    return ext[d]
def Natasha(data):


    if "how are you" in data:
        speak("I am fine")
    elif "who am i" in data:
        speak("user")
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
        t=show_ext()
        t.replace(" ","")
        s=s+"."+t
        speak("tell destination")
        d=record()
        d.replace(" ","")
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
        t=show_ext()
        t.replace(" ","")
        s=s+"."+t
        speak("tell destination")
        d=record()
        os.system("cp "+s+" "+d)
    elif "copy folder" in data:
        speak("tell source")
        s=record()
        speak("tell destination")
        d=record()
        os.system("cp -r "+s+" "+d)
    elif "kernel version" in data:
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
    elif "delete file" in data:
        speak("tell the name of file")
        n=record()
        n.replace(" ","")
        speak("tell the type of file")
        t=show_ext()
        c=n+"."+t
        os.system("rm "+c)
    elif "delete folder" in data:
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
        t=show_ext()
        t.replace(" ","")
        c=n+"."+t
        os.system("head "+c)
    elif "tail" in data:
        speak("tell the name of file")
        n = record()
        n.replace(" ", "")
        speak("tell the type of file")
        t = show_ext()
        t.replace(" ", "")
        c = n + "." + t
        os.system("tail " + c)
    elif "current directory" in data:
        os.system("pwd")
    elif "network status" in data:
        os.system("ifconfig -a")
    elif "running processes" in data:
        os.system("ps")
    elif "all processes" in data:
        os.system("ps -A")
    elif "disk usage"  in data:
        os.system("df")
    elif "file usage" in data:
        os.system("du")
    elif "login as root user" in data:
        os.system("sudo -i")
    elif "open browser" in data:
        os.system("firefox&")
    elif "give access to file" in data:
        speak("Tell the name of file")
        n=record()
        n.replace(" ","")
        speak("Tell the type of file")
        ty=show_ext()
        ty.replace(" ","")
        n=n+"."+ty
        speak("Tell the type of access")
        t=record()
        if "execute" in data:
            os.system("chmod +x "+n)
        elif "write" in data:
            os.system("chmod +w "+n)
        elif "read" in data:
            os.system("chmod +r "+n)
        else:
            os.system("chmod +xwr "+n)
    elif "add user" in data:
        speak("tell me user name")
        n = record()
        speak("are you sure to create " + n + " user")
        if ("yes"):
            os.system("sudo useradd " + n)
        else:
            speak("can't create user")
    elif "add group" in data:
        speak("tell me groub name")
        n = record()
        speak("are you sure to add " + n + "  group")
        if ("yes"):
            os.system("sudo addgroup " + n)
        else:
            speak("can't create group")
    elif "manual" in data:
        speak("manual of")
        n = record()
        os.system("man " + n)
    elif "delete user" in data:
        speak("tell me user name")
        n = record()
        speak("are you sure to delete " + n + " user")
        if ("yes"):
            os.system("sudo deluser " + n)
        else:
            speak("can't delete user")
    elif "show content" in data:
        speak("tell the name of file")
        n = record()
        n.replace(" ", "")
        speak("tell the type of file")
        t = show_ext()
        t.replace(" ", "")
        c = n + "." + t
        os.system("cat " + c)
    elif "rename file" in data:
        speak("tell filename")
        s = record()
        speak("tell the type of file")
        t = show_ext()
        t.replace(" ", "")
        s = s + "." + t
        speak("tell newname")
        d = record()
        speak("tell the type of file")
        t = show_ext()
        d.replace(" ", "")
        d = d + "." + t
        os.system("mv " + s + " " + d)
    elif "open text editor" in data:
        os.system("gedit&")
    elif "update" in data:
        os.system("sudo apt update")
    elif "upgrade" in data:
        os.system("sudo apt upgrade")
    else:
        print("Invalid Command")



time.sleep(2)
speak("Hello! I am Natasha")
flag=True
while (1):
    data=record()
    Natasha(data)


