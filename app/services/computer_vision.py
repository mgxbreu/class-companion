import requests
import cv2
from app.utils.constants import VISUAL_ANALYSIS_PATH
from app.utils.credentials import get_credentials_list 

subscription_key, endpoint = get_credentials_list("vision")

def get_photo_description(extension, photo):
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}
    response = requests.post(
        endpoint + VISUAL_ANALYSIS_PATH, headers=headers, data=cv2.imencode(extension, photo)[1].tobytes())
    analysis = response.json()

    description = analysis["description"]["captions"][0]["text"]

    return description