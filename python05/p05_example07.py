# Example for ArithmeticError (division by zero)
# We wrap this in a try-except block to handle the exception gracefully
try:
    result = 10 / 0
except ZeroDivisionError as e:  # We catch the specific ArithmeticError subclass
    print(f"Error: {e}")  # Print the error message
else:
    print(f"Result (should not print): {result}")  # This won't execute due to exception

# IndexError: accessing an index outside the list bounds
my_list = [1, 2, 3]
try:
    value = my_list[4]  # Index 4 is out of range
except IndexError as e:
    print(f"Index error: {e}")

# KeyError: accessing a non-existent key in a dictionary
my_dict = {"name": "Alice", "age": 30}
try:
    age = my_dict["city"]  # Key "city" doesn't exist
except KeyError as e:
    print(f"Key error: {e}")
