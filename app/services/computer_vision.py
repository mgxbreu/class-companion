import requests
import json
import cv2
from app.utils.constants import VISUAL_ANALYSIS_PATH

config = json.load(open("config.json"))
vision_creds = config["credentials"]["vision"]

subscription_key = vision_creds["subskey"]
endpoint = vision_creds["endpoint"]

def get_photo_description(extension, photo):
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}
    response = requests.post(
        endpoint + VISUAL_ANALYSIS_PATH, headers=headers, data=cv2.imencode('.jpg', photo)[1].tobytes())
    analysis = response.json()

    description = analysis["description"]["captions"][0]["text"]

    return description