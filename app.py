import requests
import time
from flask import Flask, render_template
TOKEN = "6994416717:AAH_qEF1vSy1gZc1nXQ4eyM4dErJshFGJaM"
chat_id = "998041732"

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    for i in range(5):
        message=f"{i}:dik"
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url)
        time.sleep(2)
    
    return render_template("index.html", title="Hello")
