import yfinance as yf


def scrape_stock_data(symbol, exchange):

    try:
        if exchange == "NSE":
            symbol = symbol + ".NS"

        stock = yf.Ticker(symbol)
        info = stock.info

        current_price = info.get("currentPrice")
        previous_close = info.get("previousClose")

        # Price Changed
        if current_price is not None and previous_close is not None:
            price_changed = round(current_price - previous_close, 2)
        else:
            price_changed = None

        # Percentage Changed
        if current_price is not None and previous_close not in (None, 0):
            percentage_changed = round(
                ((current_price - previous_close) / previous_close) * 100,
                2
            )
            percentage_changed = f"{percentage_changed}%"
        else:
            percentage_changed = None

        # Dividend Yield
        dividend = info.get("dividendYield")

        if dividend is not None:
            dividend = f"{round(dividend * 100, 2)}%"
        else:
            dividend = None

        stock_response = {
            "current_price": current_price,
            "price_changed": price_changed,
            "percentage_changed": percentage_changed,
            "previous_close": previous_close,
            "week_52_high": info.get("fiftyTwoWeekHigh"),
            "week_52_low": info.get("fiftyTwoWeekLow"),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("trailingPE"),
            "dividend_yield": dividend,
        }

        return stock_response

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None