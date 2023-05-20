from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time
from app.utils.credentials import get_credentials_list 

class ImageProcessing():

    def __init__(self):
        self.read_results = None
        self.end_text = ""
        subscription_key, endpoint = get_credentials_list("vision")
        self.computervision_client = ComputerVisionClient(
            endpoint, CognitiveServicesCredentials(subscription_key))

    def read_text_in_image(self, image_path):
        with open(image_path, mode="rb") as image_data:
            operation_id = self.get_operation_id(image_data)

            while True:
                read_results = self.computervision_client.get_read_result(operation_id)
                if read_results.status not in [OperationStatusCodes.running, OperationStatusCodes.not_started]:
                    break
                time.sleep(1)

            return self.end_text

    def get_operation_id(self, image_data):
        read_operation = self.computervision_client.read_in_stream(image_data, raw=True)
        operation_location = read_operation.headers["Operation-Location"]
        operation_id = operation_location.split("/")[-1]

        return operation_id
    
    def process_line_by_line(self):
        if self.read_results.status == OperationStatusCodes.succeeded:
            for page in self.read_results.analyze_result.read_results:
                for line in page.lines:
                    self.end_text += line.text