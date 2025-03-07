import pyttsx3
from django.template import engines

engine=pyttsx3.init()

engine.setProperty('rate',200)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


text="this is my yt channel and today we are learnig python"
engine.say(text)
engine.runAndWait()