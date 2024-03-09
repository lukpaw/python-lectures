ticket_price = input("Enter bus ticket price: ")
print("Ticket price: " + ticket_price)

number_of_students = input("Enter the number of students traveling by bus: ")

total_amount = float(ticket_price) * int(number_of_students)
print("You pay: " + str(total_amount))
