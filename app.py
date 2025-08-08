from flask import Flask, request, make_response
import os

app = Flask(__name__)

CONFIRMATION_TOKEN = os.environ.get("CONFIRMATION_TOKEN")

@app.route("/", methods=["POST"])
def vk_callback():
    data = request.get_json(force=True)
    if data.get("type") == "confirmation":
        # возвращаем строку подтверждения с кодом 200 и content-type text/plain
        response = make_response(CONFIRMATION_TOKEN, 200)
        response.headers["Content-Type"] = "text/plain"
        return response
    elif data.get("type") == "message_new":
        return "ok", 200
    return "ok", 200

@app.route("/", methods=["GET"])
def check():
    return "VK bot is running", 200
    
