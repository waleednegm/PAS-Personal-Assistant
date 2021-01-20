import datetime
import speak_fun
# get the current time
def time():
    Time_NOW=datetime.datetime.now().strftime("%I:%M:%S")
    print("the current time is "+ Time_NOW)
    speak_fun.speak("the current time is ")
    speak_fun.speak(Time_NOW)
# get the current date
def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day  = datetime.datetime.now().day
    print("the current date is "+ day +"-" + month + "-" + year  )
    speak_fun.speak("the current date is ")
    speak_fun.speak(day)
    speak_fun.speak(month)
    speak_fun.speak(year)


