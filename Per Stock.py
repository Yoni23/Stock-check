def get_stock_data(ticker):
    """
    Placeholder for real data. Replace with actual API call or database query.
    """
    mock_data = {
        "AAPL": {
            "PE": 28,
            "PB": 7,
            "DebtEquity": 1.5,
            "FreeCashflowYield": 2.3,
            "CurrentRatio": 1.0,
            "PS": 7.2,
            "ROE": 35,
            "ROIC": 27,
            "EarningGrowth": 12,
            "RevenueGrowthYOY": 8,
            "EPSGrowthYOY": 10,
            "GrossMargin": 43,
            "RevGrowthCashflowMargin": 25,
            "TAM": 1000,
            "RetentionRate": 95,
            "Moat": True,
            "InsiderBuying": False,
            "Cashflow5Yrs": True
        }
        # Add more tickers here
    }

    return mock_data.get(ticker.upper())


def classify_stock(metrics):
    """
    Classify the stock based on the given financial metrics.
    """

    if not metrics:
        return "No data found."

    # Deep Value checks
    if (metrics["PE"] < 8 and
        metrics["PB"] < 1 and
        metrics["DebtEquity"] < 0.5 and
        metrics["FreeCashflowYield"] > 8 and
        metrics["CurrentRatio"] > 1.5 and
        metrics["PS"] < 1):
        return "Deep Value"

    # Growth checks
    if (metrics["DebtEquity"] < 0.5 and
        metrics["RevenueGrowthYOY"] >= 20 and
        metrics["EPSGrowthYOY"] >= 20 and
        metrics["GrossMargin"] >= 60 and
        metrics["RevGrowthCashflowMargin"] >= 40 and
        metrics["TAM"] >= 10_000_000_000 and
        metrics["RetentionRate"] > 110 and
        metrics["Moat"] and
        metrics["Cashflow5Yrs"]):
        return "Growth"

    # Value checks
    if (metrics["PE"] < 20 and
        metrics["DebtEquity"] < 0.5 and
        metrics["ROE"] > 15 and
        metrics["ROIC"] > 12 and
        5 <= metrics["EarningGrowth"] <= 10):
        return "Value"

    return "Unclassified"


if __name__ == "__main__":
    ticker = input("Enter stock ticker: ")
    data = get_stock_data(ticker)
    result = classify_stock(data)
    print(f"{ticker.upper()} is classified as: {result}")
