from bs4 import BeautifulSoup
import websocket
import time
import json

def parse_problem_url(url: str):
    pass

def account_login(url: str, creds):
    pass

def on_message(wsapp, message):
    print(message)

p_id = 2172
c_id = "N"
s = "https://codeforces.com".split("://", 1)[1]
url = f"wss://pubsub.{s}/ws/s_{p_id}/s_{c_id}?_={int(time.time()*1000)}&tag=&time=&eventid="
wsapp = websocket.WebSocketApp(url = url, on_message = on_message)

wsapp.run_forever()
wsapp.send(json.dumps({"subscribe": "contest-channel"}))