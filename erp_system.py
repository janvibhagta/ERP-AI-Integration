
# erp_system.py
"""Simple ERP System Simulation"""
import json

class ERPSystem:
    def __init__(self, data_file):
        with open(data_file, 'r') as f:
            self.data = json.load(f)

    def get_contracts(self):
        return self.data.get("contracts", [])

    def update_contract_analysis(self, contract_id, analysis):
        for contract in self.data["contracts"]:
            if contract["id"] == contract_id:
                contract["analysis"] = analysis
        print(f"Contract {contract_id} updated with analysis: {analysis}")
