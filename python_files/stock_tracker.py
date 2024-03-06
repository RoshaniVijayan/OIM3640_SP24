from time import sleep
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
    for second in range(10):
        print(f"{yf.Ticker('AAPL').history()['Close'][-1]:.2f}")
        sleep(1)


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
        watchlist = 'AMZN NFLX FB GOOG'.split()
        display_menu()
        choice = input("Enter a menu number: ")
        if choice == '1':
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