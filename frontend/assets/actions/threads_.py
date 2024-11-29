import requests
import assets.actions.tokens



url = "http://api.whizz.guru/"

def create_theme(topic: str, title: str, text: str):
    token = assets.actions.tokens.read_token()

    headers  = {
        "Authorization": f"Bearer {token}"
    }
    
    data = {
        "topic": topic,
        "title": title,
        "text": text
    }
    
    response = requests.post(url = f"{url}/themes/", json = data, headers = headers)
    
    if response.status_code == 200:
        print(response)
        return [200, response.json()]
    elif response.status_code == 422:
        return [422, None]
    else:
        print(response.json())
    
def read_themes(limit: int | None):
    token = assets.actions.tokens.read_token()

    headers  = {
        "Authorization": f"Bearer {token}"
    }
    
    params = {
        "limit": limit,
    }
    
    response = requests.get(url = f"{url}/themes/", params = params, headers = headers)
    
    if response.status_code == 200:
        return [200, response.json()]
    elif response.status_code == 422:
        return [422]
    elif response.status_code == 400:
        return [400]
    else:
        return [0, response.json()]
    
def read_comments(post_id):
    token = assets.actions.tokens.read_token()

    headers  = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.get(url = f"{url}/comments/{post_id}", params = {"post_id": post_id}, headers = headers)
    if response.json != []:
        return [200, response.json()]
    elif response.json() == []:
        return [404, False]
    else:
        return [422]
    
def create_comment(post_id: int, token: str, text: str):
    token = assets.actions.tokens.read_token()

    headers  = {
        "Authorization": f"Bearer {token}"
    }
    
    params = {
        "post_id": post_id,
    }
    
    body = {
        "text": text,
        "parent_id": None
    }
    print(post_id, token, text)
    response = requests.post(url = f"{url}/comments/{post_id}/", params = params, json = body, headers = headers)
    if response.status_code == 200:
        return 200
    elif response.status_code == 422:
        return 422
    else:
        print(response.json())
        return False