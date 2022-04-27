import requests
from datetime import datetime

USERNAME = "joshgottlieb2"
TOKEN = "heodhsluhkju"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Push-up Tracking Graph",
    "unit": "push-ups",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2"

today = datetime.now()
print(today)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many push-ups did you do today? ")
}

pixel_response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(pixel_response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "30"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2/{today.strftime('%Y%m%d')}"
#
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
