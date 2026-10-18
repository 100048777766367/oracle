class VaultPricingBridge:
    @staticmethod
    def calculate_suggested_price(record_count, truth_confidence):
        base_price = max(4.99, round((record_count * 0.002) * truth_confidence, 2))
        return min(base_price, 49.00)
