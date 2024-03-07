# Create a list of fruits
fruits = ["apple", "banana", "cherry", "orange", "mango"]

# Check if an element exists in the list
"banana" in fruits  # Output: True
"watermelon" in fruits  # Output: False

# Check if an element does not exist in the list
"watermelon" not in fruits  # Output: True
"banana" not in fruits  # Output: False

# Find the index of the first occurrence of an element
fruits.index("mango")  # Output: 4

# Count the number of occurrences of an element
fruits.count("apple")  # Output: 1

# Iterate over the list and print the fruits that are not in the "citrus" list
citrus = ["orange", "lemon", "grapefruit"]
for fruit in fruits:
    if fruit not in citrus:
        print(fruit)
