
import os

# Токен группы ВКонтакте
GROUP_TOKEN = os.getenv("GROUP_TOKEN")

# Секретный код подтверждения для Callback API
CONFIRMATION_TOKEN = os.getenv("CONFIRMATION_TOKEN")

# Версия VK API
VK_API_VERSION = "5.131"

# ID администратора (твой VK user id)
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# ID беседы, если хочешь задать вручную (опционально)
CHAT_PEER_ID = int(os.getenv("CHAT_PEER_ID", "0"))

# Имя бота, чтобы он реагировал (например, "dizel")
BOT_NAME = os.getenv("BOT_NAME", "dizel_community").lower() 

# Статус отладки
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
