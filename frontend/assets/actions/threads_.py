import requests

url = "https://api.whizz.guru/"

def create_theme(token: str, topic: str, title: str, text: str):
    params = {
        "token": token
    }
    
    data = {
        "topic": topic,
        "title": title,
        "text": text
    }
    
    response = requests.post(url = f"{url}/themes/", params = params, json = data)
    
    if response.status_code == 200:
        return [200, response.json()]
    elif response.status_code == 422:
        return [422, None]
    
def read_themes(limit: int | None, token: str | None):
    params = {
        "limit": limit,
        "token": token
    }
    
    response = requests.get(url = f"{url}/themes/", params = params)
    
    if response.status_code == 200:
        return [200, response.json()]
    elif response.status_code == 422:
        return 422
    elif response.status_code == 400:
        return 400
    
