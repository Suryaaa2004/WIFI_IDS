import requests

BOT_TOKEN = "8529007506:AAGXX3IayGK4IOM4hIfkiAmJ14-kj3P23I0"
CHAT_ID = "Wifi_smart_home_ids_bot"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{8529007506:AAGXX3IayGK4IOM4hIfkiAmJ14-kj3P23I0}/sendMessage"
    
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram Error:", e)