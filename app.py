import os
import json
from flask import Flask, request
from config import GROUP_TOKEN, CONFIRMATION_TOKEN, BOT_NAME, ADMIN_ID
import vk_api
from vk_api.utils import get_random_id

app = Flask(__name__)

vk_session = vk_api.VkApi(token=GROUP_TOKEN)
vk = vk_session.get_api()

@app.route('/', methods=['POST'])
def callback():
    data = request.get_json(force=True)
    if data["type"] == "confirmation":
        return CONFIRMATION_TOKEN

    if data["type"] == "message_new":
        message = data["object"]["message"]
        text = message.get("text", "")
        peer_id = message["peer_id"]

        if BOT_NAME in text.lower() or f"@{BOT_NAME}" in text.lower():
            vk.messages.send(
                peer_id=peer_id,
                message="Я на месте! Слушаю внимательно.",
                random_id=get_random_id()
            )

    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)