import cv2

def write_image(image_name, frame):
    cv2.imwrite(image_name, frame)

def get_image_name(name):
    image_name = f"{name}.png"
    return image_name