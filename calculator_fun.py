import wolframalpha
import speak_fun

def calculate(something):
    walframe_id = "EKE8AU-85GYWR9E9W"
    client = wolframalpha.Client(walframe_id)
    i = something.lower().split().index("calculate")
    query = something.split()[i+1 :]
    res = client.query(''.join(query))
    answer = next(res.results).text
    speak_fun.speak("The answer is " + answer)
