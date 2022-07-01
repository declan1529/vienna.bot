from threading import Thread
from flask import Flask
import requests, time

app = Flask('')

@app.route('/')
def home():
    return "Staying Online"

def run():
  app.run(host='0.0.0.0',port=8080)

def ping():
    while True:
        time.sleep(20)
        print("ping")
        requests.get("https://viennabot.declan1529.repl.co")


def keep_alive():
    t = Thread(target=run)
    t1 = Thread(target=ping)
    t.setDaemon(True)
    t.start()
    t1.start()

keep_alive()