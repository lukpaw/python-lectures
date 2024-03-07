ticket_price = float(input("Enter bus ticket price: "))
print(f"Ticket price: {ticket_price}")

number_of_students = int(input("Enter the number of students traveling by bus: "))

total_amount = ticket_price * number_of_students
print(f"You pay: {total_amount}")