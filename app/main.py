import tkinter as tk
import cv2
import requests
import json
from PIL import Image, ImageTk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import pyttsx3
from app.text import read_text_in_image
from app.sound import say_text_outloud
from app.utils.constants import VISUAL_ANALYSIS_PATH
from app.services.computer_vision import get_photo_description

# Set up the Tkinter GUI
root = tk.Tk()
root.geometry("800x600")

# Create a label for displaying the camera image
label = tk.Label(root)
label.pack()

# Create a label for displaying the image analysis results
result_label = tk.Label(root, text="")
result_label.pack()

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
        label.config(image=photo)
        label.image = photo

        description = get_photo_description('.jpg', frame)
        img_counter = 0
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Screenshot taken")
        img_counter += 1
        
        description_from_text = read_text_in_image(img_name)
   
        if description_from_text:
            description = "Text in front of you " + description_from_text 
            result_label.config(text=description)
        

        say_text_outloud(description)
        result_label.config(text=description)

    # Schedule the next update
    root.after(10, update_frame)

# Start the update loop
update_frame()

# Start the Tkinter main loop
root.mainloop()