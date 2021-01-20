import pyttsx3

engine = pyttsx3.init()
def speak(audio):
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[1].id)  
    engine.setProperty('rate', 140)
    engine.say(audio)
    engine.runAndWait()
