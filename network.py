import requests

API = "http://127.0.0.1:5000/api"

def get_heroes():
    return requests.get(API + "/heroes").json()

def get_rank():
    return requests.get(API + "/rank").json()

def post_match(win):
    requests.post(API + "/match_result", json={"win": win})