import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 210)     # setting up new voice rate                      #printing current voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',2.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id) 
  #changing index, changes voices. 1 for female
voice = engine.getProperty('voice')  
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
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