student1 = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'email': 'alice@example.com'
}
student2 = {
    'first_name': 'Bob',
    'last_name': 'Johnson',
    'email': 'bob@example.com'
}
student3 = {
    'first_name': 'Charlie',
    'last_name': 'Brown',
    'email': 'charlie@example.com'
}

students = [student1, student2, student3]

# Print student records
for student in students:
    print(f"First Name: {student['first_name']}")
    print(f"Last Name: {student['last_name']}")
    print(f"Email: {student['email']}")
    print()  # Add an empty line for readability
