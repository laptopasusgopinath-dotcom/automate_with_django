import yfinance as yf

def scrape_stock_data(symbol, exchange):

    if exchange == "NSE":
        symbol = symbol + ".NS"

    stock = yf.Ticker(symbol)
    info = stock.info

    current_price = info.get("currentPrice")
    previous_close = info.get("previousClose")
    open_price = info.get("open")
    day_range = f"{info.get('dayLow')} - {info.get('dayHigh')}"
    week52_range = f"{info.get('fiftyTwoWeekLow')} - {info.get('fiftyTwoWeekHigh')}"
    volume = info.get("volume")
    average_volume = info.get("averageVolume")
    market_cap = info.get("marketCap")
    pe_ratio = info.get("trailingPE")

    print("Current Price ===>", current_price)
    print("Previous Close ===>", previous_close)
    print("Open ===>", open_price)
    print("Day Range ===>", day_range)
    print("52 Week Range ===>", week52_range)
    print("Volume ===>", volume)
    print("Average Volume ===>", average_volume)
    print("Market Cap ===>", market_cap)
    print("PE Ratio ===>", pe_ratio)


scrape_stock_data("AAPL", "NASDAQ")