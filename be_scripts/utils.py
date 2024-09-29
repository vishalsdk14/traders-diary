import yfinance as yf

def get_current_price(symbol, ptype):
    ticker = yf.Ticker(symbol)
    todays_data = ticker.history(period='1d')
    return todays_data.iloc[-1][ptype]
