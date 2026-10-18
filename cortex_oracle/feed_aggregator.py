import json
import urllib.request

class RealityFeedAggregator:
    @staticmethod
    def fetch_market_pulse():
        pulse = {"usd_index": 1.0, "market_sentiment": "STABLE", "connectivity": True}
        try:
            req = urllib.request.Request("https://api.github.com", headers={"User-Agent": "Oracle-Probe"})
            with urllib.request.urlopen(req, timeout=3.5) as r:
                pulse["connectivity"] = (r.status == 200)
        except Exception:
            pulse["connectivity"] = False
        return pulse
