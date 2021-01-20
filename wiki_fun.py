import wikipedia
import speak_fun as sf
def wiki(search_about):
    sentence = wikipedia.summary(search_about,sentences=4)
    print(sentence)
    sf.speak(sentence)