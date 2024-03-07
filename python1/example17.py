ticket_price = float(input("Enter bus ticket price: "))
print(f"Ticket price: {ticket_price}")

money_in_wallet = float(input("Money in the wallet: "))

number_of_students = money_in_wallet / ticket_price
# number_of_students = int(money_in_wallet / ticket_price)
print(f"Number of students traveling by bus: {number_of_students}")
