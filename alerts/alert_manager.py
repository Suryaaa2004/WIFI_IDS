from utils.logger import log_alert
from alerts.notifier import send_telegram_alert

def handle_alert(alert):
    msg = f"[ALERT] {alert['type']} | Severity: {alert['severity']}"

    print(msg)
    log_alert(alert)

    # Send Telegram Alert
    send_telegram_alert(msg)