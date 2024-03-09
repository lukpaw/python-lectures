ticket_price = float(input("Enter bus ticket price: "))
print(f"Ticket price: {ticket_price}")

number_of_students = int(input("Enter the number of students traveling by bus: "))

total_amount = ticket_price * number_of_students
print(f"You pay: {total_amount}")

money_in_wallet = float(input("Money in the wallet: "))

can_buy_tickets = money_in_wallet >= total_amount
print(type(can_buy_tickets))
print(f"Can buy tickets: {can_buy_tickets}")
