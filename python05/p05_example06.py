try:
    user_age = int(input("Enter your age: "))
    print(f"You are {user_age} years old.")
except ValueError:
    print("Invalid input. Please enter a number.")

name = input("Enter your name: ")
assert len(name) > 0, "Name cannot be empty"  # Raises AssertionError if name is empty
print(f"Your name is {name}.")
