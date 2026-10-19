import pandas as pd
from dataclasses import dataclass
from typing import Dict, List

EXCHANGE_RATES = {
    "USD": 1.0,
    "CNY": 7.25,
    "EUR": 0.92,
    "GBP": 0.79,
}

@dataclass
class TradeSummary:
    total_revenue: float
    total_cost: float
    gross_margin: float
    top_products: List[str]
    monthly_trend: Dict[str, float]
    currency: str

class TradeAnalyzer:
    def __init__(self, filepath: str, base_currency: str = "USD"):
        self.filepath = filepath
        self.currency = base_currency
        self.df = self._load(filepath)

    def _load(self, path: str) -> pd.DataFrame:
        if path.endswith(".csv"):
            return pd.read_csv(path)
        return pd.read_excel(path)

    def _convert(self, amount: float, from_currency: str) -> float:
        rate = EXCHANGE_RATES.get(from_currency.upper(), 1.0)
        base_rate = EXCHANGE_RATES.get(self.currency.upper(), 1.0)
        return round(amount / rate * base_rate, 2)

    def run(self) -> TradeSummary:
        df = self.df.copy()
        df['revenue_usd'] = df.apply(
            lambda r: self._convert(r['revenue'], r.get('currency', 'USD')), axis=1
        )
        df['cost_usd'] = df.apply(
            lambda r: self._convert(r['cost'], r.get('currency', 'USD')), axis=1
        )

        total_revenue = df['revenue_usd'].sum()
        total_cost = df['cost_usd'].sum()
        gross_margin = round((total_revenue - total_cost) / total_revenue * 100, 2)

        top_products = (
            df.groupby('product')['revenue_usd']
            .sum().sort_values(ascending=False)
            .head(5).index.tolist()
        )

        df['month'] = pd.to_datetime(df['date']).dt.to_period('M').astype(str)
        monthly = df.groupby('month')['revenue_usd'].sum().to_dict()

        return TradeSummary(
            total_revenue=total_revenue,
            total_cost=total_cost,
            gross_margin=gross_margin,
            top_products=top_products,
            monthly_trend=monthly,
            currency=self.currency,
        )