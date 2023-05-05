import numpy as np
import requests
import json
from PIL import Image, ImageTk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import azure.cognitiveservices.speech as speechsdk
import os
import pyttsx3
import time

from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes

# Load the Azure credentials from config.json
config = json.load(open("config.json"))
vision_creds = config["credentials"]["vision"]

# Set up the Computer Vision client
subscription_key = vision_creds["subskey"]
endpoint = vision_creds["endpoint"]
computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(subscription_key))


def read_text_in_image(image_path):
    # Use Read API to read text in image
    with open(image_path, mode="rb") as image_data:
        read_op = computervision_client.read_in_stream(image_data, raw=True)

        # Get the async operation ID so we can check for the results
        operation_location = read_op.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]

        # Wait for the asynchronous operation to complete
        while True:
            read_results = computervision_client.get_read_result(operation_id)
            if read_results.status not in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
                break
            time.sleep(1)

        # If the operation was successfully, process the text line by line

        complete_text = ""
        if read_results.status == OperationStatusCodes.succeeded:
            for page in read_results.analyze_result.read_results:
                for line in page.lines:
                    complete_text += line.text
                    print(line.text)
        return complete_text