from collections import defaultdict
import time
from core.config import CONFIG
from detection.base_detector import BaseDetector

class DeauthDetector(BaseDetector):
    def __init__(self):
        self.deauth_counts = defaultdict(list)

    def detect(self, packet):
        try:
            if packet.haslayer("Dot11Deauth"):
                src = packet.addr2
                now = time.time()

                self.deauth_counts[src].append(now)

                self.deauth_counts[src] = [
                    t for t in self.deauth_counts[src]
                    if now - t <= CONFIG["TIME_WINDOW"]
                ]

                count = len(self.deauth_counts[src])

                if count > CONFIG["DEAUTH_THRESHOLD"]:
                    return {
                        "type": "Deauth Attack",
                        "source": src,
                        "severity": "High",
                        "count": count
                    }
        except Exception:
            return None

        return None