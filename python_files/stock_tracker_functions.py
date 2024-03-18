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
    else:
        files = os.listdir('watchlists')
        if not files:
            print("No saved list")
        else:
            for number, file in enumerate(files, 1):
                print(f"{number} - {file[:-10]}")
            return files

def choose_list():
    lists = read_directory()
    choice = int(input("Enter watchlist number: "))
    file = lists[choice- 1]
    return open(f"watchlists/{file}" ,'r').read().split()

# read_directory()
print(choose_list())


