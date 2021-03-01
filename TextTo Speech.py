import pyttsx3
from time import strftime
from datetime import date


engine = pyttsx3.init()
current_time = strftime('%H:%M:%S %p')
today = date.today()


def say():
    engine.say(f"The current date is {today}")
    engine.say(f"The current time is {current_time}")


say()
engine.runAndWait()