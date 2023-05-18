import tkinter as tk
import cv2
import requests
import json
from PIL import Image, ImageTk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import pyttsx3
from app.classes.image_processing import ImageProcessing
from app.classes.sound import SoundEngine
from app.classes.output_interface import OutputInterface
from app.utils.constants import VISUAL_ANALYSIS_PATH, TEXT_FILE_PATH
from app.services.computer_vision import get_photo_description


sound_engine = SoundEngine("man", TEXT_FILE_PATH)
image_processing = ImageProcessing()
interface = OutputInterface("800x600")

# Create a video capture object
cap = cv2.VideoCapture(0)


pre_description= ''

def update_frame():
    # Capture a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Convert the OpenCV image to a Pillow image
        image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        # Update the label with the new image
        photo = ImageTk.PhotoImage(image)
        
        interface.update_frame(photo)

        description = get_photo_description('.jpg', frame)
        img_counter = 0
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Screenshot taken")
        img_counter += 1
        
        description_from_text = image_processing.read_text_in_image(img_name)
   
        if description_from_text:
            description = "Text in front of you " + description_from_text 
            interface.update_label(description)
        

        sound_engine.say_text_outloud(description)
        interface.update_label(description)

    interface.schedule_next_update(update_frame)

# Start the update loop
update_frame()

interface.run()