
import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "TOKEN",
    "username": "USERNAME",
    "agreeTermsOfservice": "yes",
    "notMinor": "yes",
}


USERNAME = "mollyyyyyyyy"
TOKEN = "aksjsjeuwoprhew"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)