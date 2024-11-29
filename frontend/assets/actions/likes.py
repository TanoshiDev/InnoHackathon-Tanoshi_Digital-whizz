import requests
import assets.actions.tokens



url = "https://api.whizz.guru"


def like_thread(id: int):
    token = assets.actions.tokens.read_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    params = {
        "post_id": id,
    }
    
    response = requests.post(url = f"{url}/themes/{id}/like", params = params, headers = headers)
    if response.status_code == 200:
        print(response.json())
        return True
    elif response.status_code == 422:
        print(response.json())
        return None
    elif response.status_code == 400:
        print(response.json())
        return False
    else:
        print(response)
