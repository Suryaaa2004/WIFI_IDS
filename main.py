from sniffer.packet_sniffer import start_sniffing
from detection.deauth_detector import DeauthDetector
from detection.arp_detector import ARPDetector
from core.engine import DetectionEngine
from alerts.alert_manager import handle_alert
from detection.ml_detector import MLDetector
engine = DetectionEngine([
    DeauthDetector(),
    ARPDetector(),
    MLDetector()            
])

def process_packet(packet):
    alert = engine.process(packet)
    if alert:
        handle_alert(alert)

if __name__ == "__main__":
    print("🔥 Advanced WiFi IDS/IPS Running...")
    start_sniffing(process_packet)