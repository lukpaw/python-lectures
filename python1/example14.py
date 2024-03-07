ticket_price = float(input("Enter bus ticket price: "))
print("Ticket price: " + str(ticket_price))

number_of_students = int(input("Enter the number of students traveling by bus: "))

total_amount = ticket_price * number_of_students
print("You pay: " + str(total_amount))
