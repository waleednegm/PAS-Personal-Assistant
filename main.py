import pyttsx3
import datetime
import welcome_fun as wf
import speak_fun as sf
import get_voice_command as gvc
import time_fun as tf
import wiki_fun as wikif
import browser
import search_google as sg
import search_youtube as sy
import system_operations as so
import open_dir
import translate_fun
import calculator_fun

if __name__ == "__main__":
    wf.welcome()
    # get the command and execute it
    while True:
        command = gvc.command().lower()
        if "hello" == command or "hi"==command:
            print("Hello i am here to help you")
            sf.speak("Hello i am here to help you")
        elif "time" in command:
            sf.speak(tf.time())
        elif "date" in command:
            sf.speak(tf.date())
        elif "wiki" in command:
            command=command.replace("wikipedia","")
            print("Searching Now")
            sf.speak("Searching Now")
            wikif.wiki(command)
        elif "launch" in command:
            print("whats the website you want me to launch for you ? ")
            sf.speak("whats the website you want me to launch for you ? ")
            website = gvc.command().lower()
            print("Launching ")
            sf.speak("Launching ")
            browser.open_web_com(website)
        elif "search youtube" in command:
            print("what are you want me to search in youtube for you ? ")
            sf.speak("what are you want me to search in youtube for you ? ")
            youtube_search = command.command_().lower()
            print("Ok")
            sf.speak("Ok")
            sy.search(youtube_search)
        elif "search google" in command:
            print("what are you want me to search in google for you ? ")
            sf.speak("what are you want me to search in google for you ? ")
            google_search = command.command_().lower()
            print("Ok")
            sf.speak("Ok")
            sg.search(google_search)
        elif "cpu" in command:
            sf.speak(so.cpu())
        elif "battary" in command:
            sf.speak(so.battary())
        elif "downloads" in command:
            open_dir.open_downloads()
        elif "documents" in command:
            open_dir.open_downloads()
        elif "desktop" in command:
            open_dir.open_desktop()
        elif "translate" in command:
            command = command.replace("translate","")
            print("in which language want to translate ")
            sf.speak("in which language want to translate ")
            lang= gvc.command()
            translate_fun.translate_sen(command,lang)
        elif "calculate" in command:
            calculator_fun.calculate(command)
        elif "how are you" in command:
            sf.speak("Not too bad , How are You")
        elif "i" in command and "fine" in command:
            sf.speak("That's great")
        elif "i" in command and "feel" in command and "bad":
            sf.speak("Sorry about that ")
        elif "i" in command and "feel" in command and "good":
            sf.speak("I am happy to hear that")
        elif "go offline" in command:
            sf.speak("Going oflline now")
            quit()
        else :
            print("I cant understand You , please say it again or look at commands")
            sf.speak("I cant understand You , please say it again or look at commands")