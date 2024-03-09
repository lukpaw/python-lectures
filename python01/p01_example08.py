ticket_price = float(input("Enter bus ticket price: "))
print(f"Ticket price: {ticket_price}")

money_in_wallet = float(input("Money in the wallet: "))

money_for_drinks = float(input("Money for drinks: "))

number_of_students = int((money_in_wallet - money_for_drinks) / ticket_price)
print(f"Number of students traveling by bus: {number_of_students}")