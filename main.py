import argparse
import pandas as pd
from analyzer import TradeAnalyzer
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description='Trade Flow Analyzer')
    parser.add_argument('--input', required=True, help='Input CSV/Excel file path')
    parser.add_argument('--output', required=True, help='Output directory for reports')
    parser.add_argument('--currency', default='USD', help='Base currency (default: USD)')
    args = parser.parse_args()

    print(f"[*] Loading trade data from {args.input}...")
    analyzer = TradeAnalyzer(args.input, base_currency=args.currency)
    summary = analyzer.run()

    print(f"[*] Generating report to {args.output}...")
    gen = ReportGenerator(summary, args.output)
    gen.export_excel()
    gen.export_summary_txt()

    print(f"[+] Done. Report saved to {args.output}")

if __name__ == '__main__':
    main()