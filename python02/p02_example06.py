# Create a list
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Check if an element exists in the list using the in operator
print(f"Is 'banana' in the list? {'banana' in my_list}")

# Check if an element does not exist in the list using the not in operator
print(f"Is 'mango' not in the list? {'mango' not in my_list}")

# Check if multiple elements exist in the list using the in operator
fruits_to_check = ["apple", "mango"]
print(f"Are all fruits in 'fruits_to_check' present in the list? {all(fruit in my_list for fruit in fruits_to_check)}")

# Check if any element exists in the list using the in operator
fruits_to_check = ["mango", "papaya"]
print(f"Is any fruit in 'fruits_to_check' present in the list? {any(fruit in my_list for fruit in fruits_to_check)}")
