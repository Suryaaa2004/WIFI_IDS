import json
from datetime import datetime
from core.config import CONFIG

def log_alert(alert):
    alert["timestamp"] = datetime.now().isoformat()

    with open(CONFIG["LOG_FILE"], "a") as f:
        f.write(json.dumps(alert) + "\n")