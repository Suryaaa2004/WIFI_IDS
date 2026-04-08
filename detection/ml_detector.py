from detection.base_detector import BaseDetector
from sklearn.ensemble import IsolationForest

class MLDetector(BaseDetector):
    def __init__(self):
        self.model = IsolationForest(contamination=0.05)
        self.trained = False
        self.data = []

    def extract_features(self, packet):
        try:
            length = len(packet)

            proto = 0
            if packet.haslayer("TCP"):
                proto = 1
            elif packet.haslayer("UDP"):
                proto = 2

            return [length, proto]

        except Exception:
            return None

    def detect(self, packet):
        try:
            features = self.extract_features(packet)

            if features is None:
                return None

            self.data.append(features)

            # Train model
            if len(self.data) > 50 and not self.trained:
                self.model.fit(self.data)
                self.trained = True

            if self.trained:
                pred = self.model.predict([features])
                if pred[0] == -1:
                    return {
                        "type": "Anomaly Detected (ML)",
                        "severity": "Medium",
                        "features": features
                    }

        except Exception:
            return None

        return None