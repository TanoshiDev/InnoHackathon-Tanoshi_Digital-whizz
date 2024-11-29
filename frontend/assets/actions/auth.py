import requests
import assets.actions.tokens as tokens

url = "https://api.whizz.guru/"

def register(login: str, password: str):
    json = {
        "login": login,
        "password": password
    }
    
    response = requests.post(url = f"{url}auth/registration", json = json)
    
    if response.status_code == 200:
        tokens.write_token(response.json()["token"])
        tokens.write_login(response.json()["login"])
        return 200
    elif response.status_code == 400:
        return 400
    else:
        return 422
    
def login(login: str, password: str):
    json = {
        "username": login,
        "password": password,
        "grant_type": "password",
    }
    
    response = requests.post(url = f"{url}/auth/login", data = json)
    
    if response.status_code == 200:
        tokens.write_token(response.json()["access_token"])
        print(response.json())
        return 200
        
    elif response.status_code == 400:
        return 400
    else:
        print(response.json())
        return 422

def user_info(user_id: int):
    token = tokens.read_token()
    
    headers = {
        "Authorization": f"Bearer {token}"
    }   
    
    params = {
        "user_id": user_id
    }
    
    response = requests.get(url = f"{url}/users/{user_id}", params = params, headers = headers)
    
    if response.status_code == 200:
        return response.json()