import yfinance as yf

aapl = yf.Ticker("AAPL").history()

print(aapl)