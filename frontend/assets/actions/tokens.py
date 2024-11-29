import os

current_dir = os.path.dirname(__file__)
token_path = os.path.join(current_dir, "..", "session.whz")
login_path = os.path.join(current_dir, "..", "login.whz")

def write_token(token: str):
    with open(token_path, "w") as f:
        f.write(token)
        
def read_token():
    with open(token_path, "r") as f:
        return f.readline()
        
def write_login(login: str):
    with open(login_path, "w") as f:
        f.write(login)
        
def read_login():
    with open(login_path, "r") as f:
        return f.readline()