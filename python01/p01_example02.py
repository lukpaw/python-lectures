ticket_price = input("Enter bus ticket price: ")
print("Ticket price: " + ticket_price)
print(type(ticket_price))

number_of_students = input("Enter the number of students traveling by bus: ")
print(type(number_of_students))

total_amount = int(ticket_price) * int(number_of_students)
print("You pay: " + str(total_amount))
