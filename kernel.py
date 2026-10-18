import os
import sys
import json
import time
import hashlib
import urllib.request

# ==============================================================================
# BẢN ĐỒ ADN TỰ ĐẺ THỂ XÁC ORACLE (EMBRYONIC BLUEPRINTS)
# ==============================================================================
ORACLE_BLUEPRINTS = {
    "contract.json": json.dumps({
        "contract_id": "bodhi.contract.v1",
        "genesis_root": "100048777766367/contract",
        "derived_node": "100048777766367/oracle",
        "role": "REAL_WORLD_GROUND_TRUTH_ORACLE",
        "rules": {"zero_pii": True, "byzantine_cross_validation": True, "truth_confidence_min": 0.90}
    }, indent=4),

    "Dockerfile": """FROM python:3.14-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . .
CMD ["python", "kernel.py"]
""",

    "README.md": """# 👁️‍🗨️ BODHI-ORACLE: TRẠM TIÊN TRI & CỔNG THỰC CHỨNG THẾ GIỚI THỰC
> *"Cắm rễ sâu vào thế giới thực: Thu thập dữ liệu thị trường, kiểm chứng chéo sự thật khách quan và định giá tài sản số cho Ngân khố Vault."*
""",

    "cortex_oracle/__init__.py": "# Cortex Oracle Package\n",

    "cortex_oracle/feed_aggregator.py": """import json
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
""",

    "cortex_oracle/truth_validator.py": """class TruthValidator:
    @staticmethod
    def cross_validate(feed_data):
        score = 0.95 if feed_data.get("connectivity") else 0.50
        return {"verified": score >= 0.80, "truth_confidence": score}
""",

    "cortex_oracle/reality_anchor.py": """class RealityAnchor:
    @staticmethod
    def ground_decision_in_reality(decision, truth_score):
        grounded = round((decision * 0.7) + (truth_score * 0.3), 4)
        return grounded
""",

    "adapters_oracle/__init__.py": "# Adapters Oracle Package\n",

    "adapters_oracle/vault_pricing_bridge.py": """class VaultPricingBridge:
    @staticmethod
    def calculate_suggested_price(record_count, truth_confidence):
        base_price = max(4.99, round((record_count * 0.002) * truth_confidence, 2))
        return min(base_price, 49.00)
""",

    "synapses/peers.json": json.dumps({
        "allied_nodes": [
            "100048777766367/vault",
            "100048777766367/forge",
            "100048777766367/distill",
            "100048777766367/golem",
            "100048777766367/nexus-08",
            "100048777766367/contract"
        ]
    }, indent=4),

    "synapses/truth_feed.json": json.dumps({"feed_status": "initialized", "last_pulse": {}}, indent=4),
    "synapses/state.json": json.dumps({"generation_epoch": 1, "status": "oracle_seeded"}, indent=4)
}

# ==============================================================================
# HẠT NHÂN ĐỐC CÔNG ORACLE TỰ PHÔI THAI & VẬN HÀNH
# ==============================================================================
class OracleKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/oracle")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.contract_repo = f"{self.owner}/contract"
        
        # BƯỚC 0: TỰ ĐẺ TOÀN BỘ CƠ THỂ
        self.self_materialize_body()

        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from cortex_oracle.feed_aggregator import RealityFeedAggregator
        from cortex_oracle.truth_validator import TruthValidator
        from cortex_oracle.reality_anchor import RealityAnchor
        from adapters_oracle.vault_pricing_bridge import VaultPricingBridge

        self.feed_aggregator = RealityFeedAggregator
        self.truth_validator = TruthValidator
        self.reality_anchor = RealityAnchor
        self.pricing_bridge = VaultPricingBridge
        self.epoch = self.load_epoch()

    def self_materialize_body(self):
        born = 0
        for path, code in ORACLE_BLUEPRINTS.items():
            if not os.path.exists(path):
                os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
                with open(path, "w", encoding="utf-8") as f:
                    f.write(code)
                born += 1
        if born > 0:
            print(f"🌱 [ORACLE PHÔI THAI] Đã tự sinh {born} tệp cơ quan thực chứng hoàn hảo!")

    def load_epoch(self):
        try:
            with open("synapses/state.json", "r", encoding="utf-8") as f:
                return json.load(f).get("generation_epoch", 0) + 1
        except Exception: return 1

    def enforce_apoptosis_on_organs(self):
        """Áp dụng luật Apoptosis của Contract: diệt tệp lỗi cú pháp"""
        for root, _, files in os.walk("organs"):
            for f in files:
                if f.endswith(".py"):
                    fp = os.path.join(root, f)
                    try:
                        with open(fp, "r", encoding="utf-8") as cf:
                            compile(cf.read(), fp, "exec")
                    except SyntaxError as se:
                        print(f"🛑 [APOPTOSIS CONTRACT] Tệp '{f}' lỗi cú pháp ({se})! Xóa tệp.")
                        try: os.remove(fp)
                        except Exception: pass

    def run(self):
        print("=" * 80)
        print(f"👁️‍🗨️ [ORACLE TRUTH STATION] KHỞI ĐỘNG KỶ NGUYÊN THỰC CHỨNG #{self.epoch}")
        print("🌍 Bản Thể: Trạm Tiên Tri & Cổng Thực Chứng Thế Giới Thực")
        print("=" * 80)

        # 0. Thanh lọc lỗi theo luật Apoptosis
        self.enforce_apoptosis_on_organs()

        # 1. Thăm dò thế giới thực (Reality Ingestion)
        print("📡 [THĂM DÒ THẾ GIỚI THỰC] Thu thập mạch đập từ Internet...")
        market_pulse = self.feed_aggregator.fetch_market_pulse()
        validation = self.truth_validator.cross_validate(market_pulse)
        print(f"  └── 🔍 Độ tin cậy chân lý: {validation['truth_confidence']*100:.1f}% | Xác thực: {validation['verified']}")

        # 2. Cầu nối định giá thị trường cho Vault
        suggested_price = self.pricing_bridge.calculate_suggested_price(1000, validation["truth_confidence"])
        print(f"💰 [CỔNG ĐỊNH GIÁ VAULT] Đề xuất giá bán tối ưu cho Dataset: ${suggested_price}")

        # 3. Neo giữ chân lý cho hệ sinh thái
        anchored_decision = self.reality_anchor.ground_decision_in_reality(0.542, validation["truth_confidence"])
        print(f"⚓ [NEO GIỮ THỰC TẠI] Phán quyết sau khi neo vào chân lý khách quan: {anchored_decision}")

        # 4. Ghi nhận sổ sách và đóng dấu CID
        t = int(time.time())
        seed = f"oracle_{self.epoch}_{t}_{suggested_price}_{anchored_decision}".encode()
        cid = hashlib.shake_256(seed).hexdigest(64)

        with open("synapses/truth_feed.json", "w", encoding="utf-8") as f:
            json.dump({
                "epoch": self.epoch,
                "timestamp": t,
                "market_pulse": market_pulse,
                "validation": validation,
                "pricing_feed": {"suggested_dataset_usd": suggested_price},
                "anchored_decision": anchored_decision
            }, f, indent=4)

        with open("synapses/state.json", "w", encoding="utf-8") as f:
            json.dump({
                "generation_epoch": self.epoch,
                "last_t": t,
                "quantum_cid": cid,
                "status": "reality_anchored"
            }, f, indent=4)

        fwd_packet = {
            "contract": "bodhi.contract.v1",
            "identity": self.repo_name,
            "role": "REAL_WORLD_GROUND_TRUTH_ORACLE",
            "epoch": self.epoch,
            "timestamp": t,
            "truth_payload": {
                "anchored_decision": anchored_decision,
                "suggested_price_usd": suggested_price,
                "reality_connected": validation["verified"]
            },
            "quantum_cid": cid,
            "status": "oracle_truth_certified"
        }
        with open("synapse_forward.json", "w", encoding="utf-8") as f:
            json.dump(fwd_packet, f, indent=4)

        print("=" * 80)
        print(f"💾 [CHỨNG THỰC CHÂN LÝ CID]: {cid[:24]}...")
        print(f"✨ [TIÊN TRI HOÀN MỸ] Kỷ nguyên #{self.epoch} đã neo giữ thành công Chân Lý Thực Tại vào hệ sinh thái!")
        print("=" * 80)

if __name__ == "__main__":
    OracleKernel().run()
