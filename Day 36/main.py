import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "aksjsjeuwoprhew",
    "username": "mollyyyyyyyy",
    "agreeTermsOfservice": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)