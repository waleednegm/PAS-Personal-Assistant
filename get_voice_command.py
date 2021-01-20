import speech_recognition as sr
import speak_fun

def command():
    s=sr.Recognizer()
    command=""
    with sr.Microphone() as source:
        print("Listening")
        speak_fun.speak("I'm listening")
        s.pause_threshold = 1
        sound = s.listen(source)

    try:
        print("Recognizing")
        command =s.recognize_google(sound,language="en-Us")
        print(command)
    except Exception as ex:
        print(ex) 
    return command
