import cv2
from PIL import Image, ImageTk

class ImageConversion():

    def __init__(self):
        self.frame = None
        self.ret = None
        self.processed_photo = None

    def take_picture(self):
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()
        self.frame = frame
        self.ret
        cv2.imwrite("image.jpg", frame)
        return self.frame

    def convert_opencv_to_pillow(self):
        image = Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        # Update the label with the new image
        processed_photo = ImageTk.PhotoImage(image)
        processed_photo = ImageTk.PhotoImage(processed_photo)
        return self.processed_photo
    
    def convert_to_displayable_photo(self):
        if self.ret:
            self.convert_opencv_to_pillow()
            return self.processed_photo
        return