import os
from time import sleep, time
import sys
import yfinance as yf


def display_menu():
    print("""
    1. Track Watchlist
    2. Add Watchlist
    3. Edit Watchlist
    4. Delete Watchlist
    5. Exit
    """)

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


def add_list():
    #TODO write adding list functionality
    print("Add a new list!")


def edit_list():
    #TODO write logic for adding/deleteing from list
    print("Edit a list!")


def delete():
    #TODO write logic for deleting a list
    print("Delete a list!")



actions = {'2': add_list, '3': edit_list, '4': delete}
def main():
    print("Welcome to StockTraker!")
    while True:

        display_menu()
        choice = input("Enter a menu number: ")
        if choice == '1':
            watchlist = choose_list()
            track(watchlist)
        elif choice in '234':
            actions[choice]()
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Enter a valid menu number!")

if __name__ == "__main__":
    main()