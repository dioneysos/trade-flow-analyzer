# trade-flow-analyzer

A Python tool for automating foreign trade data analysis, generating structured reports from raw export/import records.

## Features
- Parse Excel/CSV trade records from multiple suppliers
- Auto-calculate profit margins, currency conversion, and volume trends
- Generate formatted Excel reports with charts
- Email report delivery via SMTP

## Quick Start
```bash
pip install -r requirements.txt
python main.py --input data/sample.csv --output reports/
```

## Project Structure
```
trade-flow-analyzer/
├── main.py
├── analyzer.py
├── report_generator.py
├── requirements.txt
└── data/
    └── sample.csv
```

## Tech Stack
- Python 3.10+
- Pandas, openpyxl
- Matplotlib (charts)
- smtplib (email delivery)