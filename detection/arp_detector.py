from scapy.all import ARP
from detection.base_detector import BaseDetector

class ARPDetector(BaseDetector):
    def __init__(self):
        self.ip_mac_map = {}

    def detect(self, packet):
        try:
            if packet.haslayer(ARP) and packet.op == 2:
                ip = packet.psrc
                mac = packet.hwsrc

                if ip in self.ip_mac_map and self.ip_mac_map[ip] != mac:
                    return {
                        "type": "ARP Spoofing",
                        "source_ip": ip,
                        "severity": "High",
                        "old_mac": self.ip_mac_map[ip],
                        "new_mac": mac
                    }

                self.ip_mac_map[ip] = mac
        except Exception:
            return None

        return None