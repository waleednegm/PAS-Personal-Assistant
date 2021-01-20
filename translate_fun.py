from googletrans import Translator
import speak_fun
def translate_sen(sentence,to_lang):
    translator = Translator()
    try:
        translator = Translator()
        translated = translator.translate(sentence,dest=to_lang).pronunciation
        print(translated)
        speak_fun.speak(translated)
    except Exception as ex:
        print("Something Wrong"+ex)
        speak_fun.speak("Something Wrong")

