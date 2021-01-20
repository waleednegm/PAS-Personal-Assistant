import speech_recognition as sr

def command():
    s=sr.Recognizer()
    command=""
    with sr.Microphone() as source:
        print("Listening")
        s.pause_threshold = 1
        sound = s.listen(source)

    try:
        print("Recognizing")
        command =s.recognize_google(sound,language="en-Us")
        print(command)
    except Exception as ex:
        print(ex) 
    return command
