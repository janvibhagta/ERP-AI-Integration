
# integrate.py
from erp_system import ERPSystem
from ai_module import AIContractAnalyzer

def main():
    erp = ERPSystem("sample_data.json")
    analyzer = AIContractAnalyzer()

    for contract in erp.get_contracts():
        analysis = analyzer.analyze(contract["text"])
        erp.update_contract_analysis(contract["id"], analysis)

if __name__ == "__main__":
    main()
