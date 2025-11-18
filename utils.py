from bs4 import BeautifulSoup
import websocket

def parse_problem_url(url: str):
    pass

def account_login(url: str, creds):
    pass

def on_message(wsapp, message):
    print(message)
wsapp = websocket.WebSocketApp(on_message = on_message)
wsapp.connect("wss://pubsub.codeforces.com/ws/")
wsapp.run_forever()

