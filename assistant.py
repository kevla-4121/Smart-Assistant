import os
import time
import speech_recognition as sr
import pyttsx3
pyttsx3.speak("welcome  ")
pyttsx3.speak("my name is maxie")
print("***********************************************************")
print("                        welcome                            ")
print("***********************************************************")
pyttsx3.speak("how can i help you")


while True:
    
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("tell me what can I open for you")
        audio = r.listen(source)
        pyttsx3.speak("opening your app")
        print("opening your app")
    p = r.recognize_google(audio)

    if(("run" in p) or ("open" in p)) and (("chrome" in p) or ("Google" in p) or("browser" in p)):
        os.system("chrome")
        time.sleep(5)
    elif(("run" in p)or ("open" in p)) and (("editor" in p) or ("Notepad" in p)):
        os.system("notepad")
        time.sleep(5)
    elif(("run" in p)or ("open" in p) or ("play" in p)) and (("song" in p)  or ("spotify" in p)):
        os.system("spotify")
        time.sleep(3)
       
    elif("calculator" in p):
        os.system("calc")
        time.sleep(5)
    elif("camera" in p):
        os.system("start microsoft.windows.camera:")
        time.sleep(5)
    elif(("alarm" in p) or ("clock" in p)):
        os.system(" start ms-clock:" )
        time.sleep(5)
    elif("calendar" in p):
        os.system("start outlookcal:")
        time.sleep(5)
    elif(("reader" in p) or ("edge" in p)):
        os.system("start microsoft-edge:")
        time.sleep(5)
    elif("mail" in p):
        os.system("start outlookmail:")
        time.sleep(5)
    elif("exit" in p)or ("quit" in p):
        print("bbye!!!! see you soon")
        pyttsx3.speak("Bbye    see you soon")
        break
    else:
        print("try again")
       
