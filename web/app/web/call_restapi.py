"""
Call REST API
"""
import requests


HOST = "127.0.0.1"
PORT = "5001"
BASE_API_URL = "http://{}:{}/api".format(HOST, PORT)


def call_api_get_saved_novels(username, password):
    inp = {}
    inp["username"] = username
    inp["password"] = password

    base_url = "{}/{}".format(BASE_API_URL, "get_saved_novel")
    params = {
        "Content-Type": "application/json"
    }
    resp = requests.get(base_url, params=params, json=inp)
    return resp.status_code, resp.json()

