import pyttsx3
engine = pyttsx3.init()

""" RATE"""
engine.setProperty('rate', 210)

"""VOLUME"""
engine.setProperty('volume', 1) 

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


def save_text(text):
    with open("text.txt", "w") as f:
        f.write(text)

def read_text():
    with open("text.txt", "r") as f:
        return f.read()

def say_text_outloud(text):
    previous_text = read_text()
    if previous_text != text:
      engine.say(text)
      save_text(text)
      engine.runAndWait()
      engine.stop()