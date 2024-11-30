from flask import Flask
from flask import request
from threading import Thread
import time
import requests

app = Flask('')


@app.route('/')
def home():
  return "I'm alive"


def run():
  app.run(host='0.0.0.0', port=80)


def keep_alive():
  t = Thread(target=run)
  t.start()


def ping_self():
  while True:
    try:
      requests.get(
          "https://22bea987-f52f-4ef8-9020-6b4089dcb8cc-00-isplf5f9wlnr.pike.replit.dev/"
      )
      print("Self-ping successful")
    except Exception as e:
      print(f"Self-ping failed: {e}")
    time.sleep(240)  # Каждые 4 минуты


if __name__ == "__main__":
  t1 = Thread(target=run)
  t2 = Thread(target=ping_self)
  t1.start()
  t2.start()
