class RealityAnchor:
    @staticmethod
    def ground_decision_in_reality(decision, truth_score):
        grounded = round((decision * 0.7) + (truth_score * 0.3), 4)
        return grounded
