from flask import Flask, request, make_response
import os

app = Flask(__name__)

CONFIRMATION_TOKEN = os.environ.get("CONFIRMATION_TOKEN")
GROUP_TOKEN = os.environ.get("GROUP_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME", "dizel")

@app.route("/", methods=["POST"])
def vk_callback():
    data = request.get_json(force=True)
    if data.get("type") == "confirmation":
        # Возвращаем токен с кодом 200
        return make_response(CONFIRMATION_TOKEN, 200)
    elif data.get("type") == "message_new":
        # Обработка сообщений
        return make_response("ok", 200)
    return make_response("ok", 200)

@app.route("/", methods=["GET"])
def check():
    return "VK bot is running", 200
    
