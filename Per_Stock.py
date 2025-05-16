import yfinance as yf
from tabulate import tabulate

# Define the criteria from your table
criteria = {
    "PE": {"Deep Value": lambda x: x < 8, "Value": lambda x: x < 20},
    "PB": {"Deep Value": lambda x: x < 1},
    "Debt/Equity": {"Deep Value": lambda x: x < 0.5, "Value": lambda x: x < 0.5, "Growth": lambda x: x < 0.5},
    "Free Cashflow yield": {"Deep Value": lambda x: x > 8},
    "Current ratio": {"Deep Value": lambda x: x > 1.5},
    "P/S": {"Deep Value": lambda x: x < 1},
    "ROE": {"Value": lambda x: x > 15},
    "ROIC": {"Value": lambda x: x > 12},
    "Earning Growth": {"Value": lambda x: 5 <= x <= 10},
    "Revenue Growth YOY": {"Growth": lambda x: x > 20},
    "EPS Growth YOY": {"Growth": lambda x: x > 20},
    "Gross margin": {"Growth": lambda x: x > 60},
    "Revenue Growth + Cash flow Margin": {"Growth": lambda x: x > 40},
    "TAM": {"Growth": lambda x: x > 10_000_000_000},
    "Retention Rate": {"Growth": lambda x: x > 110},
    "Moat": {"Growth": lambda x: x is True},
    "Cashflow 5 Years": {"Growth": lambda x: x is True},
    "Insider Buying": {"Deep Value": lambda x: x is True}
}

# Fetch financials
def fetch_data(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info

    # Example mock/placeholder values for some unavailable fields
    data = {
        "PE": info.get("trailingPE", 0),
        "PB": info.get("priceToBook", 0),
        "Debt/Equity": info.get("debtToEquity", 999),
        "Free Cashflow yield": (info.get("freeCashflow", 0) / info.get("marketCap", 1)) * 100,
        "Current ratio": info.get("currentRatio", 0),
        "P/S": info.get("priceToSalesTrailing12Months", 0),
        "ROE": info.get("returnOnEquity", 0) * 100,
        "ROIC": 0,  # Placeholder
        "Earning Growth": info.get("earningsQuarterlyGrowth", 0) * 100,
        "Revenue Growth YOY": info.get("revenueGrowth", 0) * 100,
        "EPS Growth YOY": info.get("earningsGrowth", 0) * 100,
        "Gross margin": info.get("grossMargins", 0) * 100,
        "Revenue Growth + Cash flow Margin": 0,  # Placeholder
        "TAM": 20_000_000_000,  # Placeholder
        "Retention Rate": 120,  # Placeholder
        "Moat": True,  # Placeholder
        "Cashflow 5 Years": True,  # Placeholder
        "Insider Buying": False  # Placeholder
    }

    return data

# Evaluate each metric
def evaluate(data):
    table = []
    match_counts = {"Deep Value": 0, "Value": 0, "Growth": 0}

    for metric, values in data.items():
        row = [metric, f"{values:.2f}" if isinstance(values, (float, int)) else str(values)]
        for category in ["Deep Value", "Value", "Growth"]:
            rule = criteria.get(metric, {}).get(category)
            if rule and rule(values):
                row.append("✅")
                match_counts[category] += 1
            else:
                row.append("")
        table.append(row)

    return table, match_counts

# Main
if __name__ == "__main__":
    ticker = input("Enter stock ticker: ").upper()
    data = fetch_data(ticker)
    table, counts = evaluate(data)

    headers = ["Metric", "Value", "Deep Value", "Value", "Growth"]
    print(f"\n📊 Analysis for {ticker}\n")
    print(tabulate(table, headers=headers, tablefmt="grid"))

    # Classification logic
    classification = max(counts, key=counts.get)
    print(f"\n📌 Classification: {ticker} is classified as **{classification}** (matches: {counts})")
