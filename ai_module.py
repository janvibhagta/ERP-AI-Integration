
# ai_module.py
"""Simple AI module for contract analysis"""
import re

class AIContractAnalyzer:
    def analyze(self, text):
        # Simple keyword spotting as a stand-in for AI/NLP model
        clauses = {
            "payment_terms": bool(re.search(r"payment within \\d+ days", text.lower())),
            "termination_clause": "termination" in text.lower(),
            "confidentiality": "confidential" in text.lower()
        }
        risk_score = sum(clauses.values()) / len(clauses)
        return {
            "clauses_found": clauses,
            "risk_score": round(risk_score, 2)
        }
