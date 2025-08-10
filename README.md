
# AI-Powered ERP Integration Demo

## Overview
This project demonstrates a basic integration between a simulated ERP system and an AI-powered contract analysis module.
It scans contracts in the ERP and flags key clauses, assigning a risk score.

## Features
- Simulated ERP data in JSON format
- AI module detecting payment terms, termination clauses, and confidentiality clauses
- Integration script to update ERP with analysis results

## How to Run
1. Ensure Python 3 is installed.
2. Clone or unzip the project folder.
3. Run:
   ```bash
   python integrate.py
   ```
4. View the updated contract analyses in the console output.

## Files
- `erp_system.py`: Simulated ERP system
- `ai_module.py`: Simple AI contract analyzer
- `integrate.py`: Integration script
- `sample_data.json`: Sample ERP data
