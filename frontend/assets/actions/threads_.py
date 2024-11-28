import requests

url = "http://api.whizz.guru/"

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
    
def read_comments(post_id):
    response = requests.get(url = f"{url}/comments/{post_id}", params = {"post_id": post_id})
    if response.json != []:
        return [200, response.json()]
    elif response.json() == []:
        return [404, False]
    else:
        return [422]
    
def create_comment(post_id: int, token: str, text: str):
    params = {
        "post_id": post_id,
        "token": token
    }
    
    body = {
        "text": text,
        "parent_id": None
    }
    print(post_id, token, text)
    response = requests.post(url = f"{url}/comments/{post_id}/", params = params, json = body)
    if response.status_code == 200:
        return 200
    elif response.status_code == 422:
        return 422
    else:
        return False