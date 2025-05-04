import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/")
def home():
    return "Bot is live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    message = data.get("message", "Сигнал без текста")

    if TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": message}
        requests.post(url, json=payload)

    return "OK"

# --- ЭТО ГЛАВНОЕ: запуск с правильным портом ---
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
