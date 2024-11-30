from flask import Flask
from threading import Thread
import time
import requests
import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive"

def run():
    port = os.environ.get('PORT', 80)  # Используйте PORT из окружения или 80 по умолчанию
    app.run(host='0.0.0.0', port=port)

def ping_self():
    while True:
        try:
            requests.get("https://<ваша ссылка>.replit.dev/")
            print("Self-ping successful")
        except Exception as e:
            print(f"Self-ping failed: {e}")
        time.sleep(240)

def keep_alive():
    t1 = Thread(target=run)
    t2 = Thread(target=ping_self)
    t1.start()
    t2.start()
