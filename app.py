from flask import Flask, request
import os

app = Flask(__name__)

CONFIRMATION_TOKEN = os.environ.get("CONFIRMATION_TOKEN")
GROUP_TOKEN = os.environ.get("GROUP_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME", "dizel")

@app.route("/", methods=["POST"])
def vk_callback():
    data = request.get_json()
    if data["type"] == "confirmation":
        # Возвращаем строку подтверждения без кавычек и оберток
        return CONFIRMATION_TOKEN
    elif data["type"] == "message_new":
        # Здесь можно обрабатывать новые сообщения
        return "ok"
    return "ok"

@app.route("/", methods=["GET"])
def check():
    return "VK bot is running"
        
