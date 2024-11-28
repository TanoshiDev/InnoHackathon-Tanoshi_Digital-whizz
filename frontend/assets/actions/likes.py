import requests

url = "https://api.whizz.guru"

def like_thread(id: int, token: str):
    params = {
        "post_id": id,
        "token": token
    }
    
    response = requests.post(url = f"{url}/themes/{id}/like", params = params)
    print(response.status_code)
    if response.status_code == 200:
        return True
    elif response.status_code == 422:
        return None
    elif response.status_code == 400:
        return False
