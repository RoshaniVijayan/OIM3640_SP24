import os
from time import sleep, time
import yfinance as yf
# track list
"""
1. allow continous tracking of a list of stocks
2. allow user to choose which list 
"""
watchlist = 'AMZN NFLX META GOOG'.split()
def track(watchlist):
    start = time()
    while True:
        try:
            for symbol in watchlist:
                print(f"{symbol:8}{yf.Ticker(symbol).history()['Close'][-1]:.2f}")
                sleep(1)
        except:
            print("not found")
        if time() - start >= 15:
            prompt = input("Enter to continue, any key to quit: ")
            start = time()
            if prompt:
                break
def read_directory():
    if not os.path.exists('watchlists'):
        print("No watchlist directory, creating")
        os.mkdir('watchlists')

read_directory()
print(os.listdir('watchlists'))

track(watchlist)

