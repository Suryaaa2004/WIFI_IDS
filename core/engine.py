class DetectionEngine:
    def __init__(self, detectors):
        self.detectors = detectors

    def process(self, packet):
        for detector in self.detectors:
            try:
                alert = detector.detect(packet)
                if alert:
                    return alert
            except Exception:
                continue
        return None