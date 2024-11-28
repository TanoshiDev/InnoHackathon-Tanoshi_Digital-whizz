def write_token(token: str):
    with open("frontend/assets/token.whz", "w") as f:
        f.write(token)
        
def read_token():
    with open("frontend/assets/token.whz", "r") as f:
        return f.readline()
        
def write_login(login: str):
    with open("frontend/assets/login.whz", "w") as f:
        f.write(login)
        
def read_login():
    with open("frontend/assets/login.whz", "r") as f:
        return f.readline()