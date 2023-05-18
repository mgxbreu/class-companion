import cv2
from PIL import Image, ImageTk

class ImageConversion():

    def __init__(self):
        self.frame = None
        # self.ret = None
        self.processed_photo = None
        self.capture = None

    def take_picture(self):
        self.capture = cv2.VideoCapture(0)
        return self.capture

    def get_frame(self):
        ret, frame = self.capture.read()
        self.frame = frame if ret else None
        return self.frame

    def convert_opencv_to_pillow_image(self):
        image = Image.fromarray(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))
        self.processed_photo = ImageTk.PhotoImage(image)
    
    def convert_to_displayable_photo(self):
        if self.ret:
            self.convert_opencv_to_pillow()
            return self.processed_photo
        return