import yfinance as yf

def fetch_financials(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    try:
        return {
            "PE": info.get("trailingPE", 0),
            "PB": info.get("priceToBook", 0),
            "DebtEquity": info.get("debtToEquity", 999),
            "FreeCashflowYield": (info.get("freeCashflow", 0) / info.get("marketCap", 1)) * 100,
            "CurrentRatio": info.get("currentRatio", 0),
            "PS": info.get("priceToSalesTrailing12Months", 0),
            "ROE": info.get("returnOnEquity", 0) * 100,
            "ROIC": 0,  # Not provided by yfinance directly
            "EarningGrowth": info.get("earningsQuarterlyGrowth", 0) * 100,
            "RevenueGrowthYOY": info.get("revenueGrowth", 0) * 100,
            "EPSGrowthYOY": info.get("earningsGrowth", 0) * 100,
            "GrossMargin": info.get("grossMargins", 0) * 100,
            "RevGrowthCashflowMargin": 0,  # Approximate or manually calculated
            "TAM": 10_000_000_000,  # Placeholder
            "Retention
