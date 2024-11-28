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
        "login": login,
        "password": password
    }
    
    response = requests.post(url = f"{url}/auth/login", json = json)
    
    if response.status_code == 200:
        tokens.write_token(response.json()["token"])
        return 200
    elif response.status_code == 400:
        return 400
    else:
        return 422