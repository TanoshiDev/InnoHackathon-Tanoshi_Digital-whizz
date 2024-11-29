import requests
from .tokens import read_token

def send_feedback(title: str, description: str):
    url = "https://api.whizz.guru/feedback/"
    
    token = read_token()
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    params = {
        "title": title,
        "description": description
    }
    
    response = requests.post(url = url, json = params, headers = headers)
    print(response.json())
    return response.status_code