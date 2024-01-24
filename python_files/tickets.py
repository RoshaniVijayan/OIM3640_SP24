# ticket sales calculator
STATE_TAX = .0625
CITY_TAX = .0075

print("Welcome to the ticket tabulator")
number_tickets = int(input("Enter number of tickets:\n"))
price = float(input("Enter Price:\n"))

ticket_cost = number_tickets * price
state_tax = STATE_TAX * ticket_cost
city_tax = CITY_TAX * ticket_cost
total = ticket_cost + state_tax + city_tax

print("Ticket cost: %15.2f" %(ticket_cost))
print("{:13s}{:15.2f}".format('State Tax:', state_tax))
print(f"City tax: {city_tax:18.2f}")
print(f"{'Total Cost:':^15}{total:^15,.2f}")
