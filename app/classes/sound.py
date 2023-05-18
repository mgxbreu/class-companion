import pyttsx3
from app.utils.constants import TEXT_FILE_PATH
from app.utils.file_reading import save_text, read_text

class SoundEngine():

    def __init__(self, gender: "woman" or "man", file_path):
        self.engine = pyttsx3.init()
        normal_voice_rate = 210
        self.engine.setProperty('rate', normal_voice_rate)
        maximum_volume = 1
        self.engine.setProperty('volume', maximum_volume)
        voices = self.engine.getProperty('voices')
        gender_index = 0 if gender == "woman" else 1
        self.engine.setProperty('voice', voices[gender_index].id)
        self.file_path = file_path

    def say_text_outloud(self, text):
        previous_text = read_text(self.file_path)
        if previous_text != text:
            self.engine.say(text)
            save_text(self.file_path, text)
            self.engine.runAndWait()
            self.engine.stop()
        
