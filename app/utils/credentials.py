import json

def get_service_credentials(service):
    config = json.load(open("config.json"))
    credentials = config["credentials"][service]
    return credentials

def get_credentials_list(service):
    credentials = get_service_credentials(service)
    credentials_list = list(credentials.values())
    return credentials_list


