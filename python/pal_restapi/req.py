import requests
import json

base_url = "http://localhost:8212/v1/api/"

get_headers = {
    'Accept': 'application/json',
    'Authorization': 'Basic YWRtaW46MjIxMTUz'
}

post_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic YWRtaW46MjIxMTUz'
}

def get_res(url, payload={}):
    try:
        response = requests.request("GET", url, headers=get_headers, data=payload)
    except requests.exceptions.ConnectionError:
        response = None
    return response

def post_res(url, payload={}):
    try:
        response = requests.request("POST", url, headers=post_headers, data=payload)
    except requests.exceptions.ConnectionError:
        response = None
    return response

def get_info():
    url = base_url + "info"
    response = get_res(url)
    return response

def get_players():
    url = base_url + "players"
    response = get_res(url)
    return response

def get_settings():
    url = base_url + "settings"
    response = get_res(url)
    return response

def get_metrics():
    url = base_url + "metrics"
    response = get_res(url)
    return response

def post_announce(message):
    url = base_url + "announce"
    payload = json.dumps({
        "message": message
    })
    response = post_res(url, payload)
    return response

def post_kick(userid, message="You have been kicked."):
    url = base_url + "kick"
    payload = json.dumps({
        "userid": userid,
        "message": message
    })
    response = post_res(url, payload)
    return response

def post_ban(userid, message="You have been banned."):
    url = base_url + "ban"
    payload = json.dumps({
        "userid": userid,
        "message": message
    })
    response = post_res(url, payload)
    return response

def post_unban(userId):
    url = base_url + "unban"
    payload = json.dumps({
        "userid": userId
    })
    response = post_res(url, payload)
    return response

def post_save():
    url = base_url + "save"
    response = post_res(url)
    return response

def post_shutdown(waitTime, message="Server will shutdown in $d seconds."):
    url = base_url + "shutdown"
    payload = json.dumps({
        "waittime": waitTime,
        "message": message.replace("$d", str(waitTime))
    })
    response = post_res(url, payload)
    return response

def post_stop():
    url = base_url + "stop"
    response = post_res(url)
    return response

