ticket_price = float(input("Enter bus ticket price: "))
print(f"Ticket price: {ticket_price}")

money_in_wallet = float(input("Money in the wallet: "))

money_for_drinks = float(input("Money for drinks: "))

money_for_tickets = money_in_wallet - money_for_drinks
number_of_students = int(money_for_tickets / ticket_price)
money_left_in_wallet = float(money_for_tickets % ticket_price)

money_found_in_pocket = float(input("Money found in pocket: "))
money_left_in_wallet = money_left_in_wallet + money_found_in_pocket
# money_left_in_wallet += money_found_in_pocket

print(f"Number of students traveling by bus: {number_of_students}")
print(f"Money left in the wallet: {money_left_in_wallet}")
