# Create a list
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the list
print(f"List: {my_list}")

# Slicing lists
# Get all elements from the beginning to the third element (excluding the fourth)
sliced_list = my_list[:3]
print(f"Sliced list (first three elements): {sliced_list}")

# Get all elements from the second element to the end
sliced_list = my_list[2:]
print(f"Sliced list (from second element to the end): {sliced_list}")

# Get every other element starting from the beginning
sliced_list = my_list[::2]
print(f"Sliced list (every other element): {sliced_list}")

# Common list methods
# Add an element to the end of the list
my_list.append("fig")
print(f"List after appending an element: {my_list}")

# Remove the last element from the list
my_list.pop()
print(f"List after removing the last element: {my_list}")

# Reverse the order of the list
my_list.reverse()
print(f"List after reversing: {my_list}")

# Check if an element exists in the list
print(f"Is 'banana' in the list? {'banana' in my_list}")

# Get the index of the first occurrence of an element
print(f"Index of 'cherry' in the list: {my_list.index('cherry')}")

# Count the number of occurrences of an element
print(f"Number of 'apple' occurrences in the list: {my_list.count('apple')}")

# Sort the list in ascending order
my_list.sort()
print(f"List after sorting: {my_list}")

# Clear the list
my_list.clear()
print(f"List after clearing: {my_list}")
