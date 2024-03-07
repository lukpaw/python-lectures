# Declare a list
my_list = ["apple", "banana", "pear", "orange", "plum"]

# Print the list
print(f"List: {my_list}")

# Indexing and accessing elements
print(f"First element: {my_list[0]}")  # 'apple'
print(f"Last element: {my_list[-1]}")  # 'plum'
print(f"Element at index 2: {my_list[2]}")  # 'pear'

# List operations
# Append an element at the end
my_list.append("kiwi")
print(f"List after appending an element: {my_list}")

# Delete an element at index 1
del my_list[1]
print(f"List after deleting an element: {my_list}")

# Insert an element at index 2
my_list.insert(2, "mango")
print(f"List after inserting an element: {my_list}")

# Concatenating lists
another_list = ["pineapple", "grape"]
my_list.extend(another_list)
print(f"List after concatenation: {my_list}")

# Sorting the list
my_list.sort()
print(f"List after sorting: {my_list}")

# Reversing the list
my_list.reverse()
print(f"List after reversing: {my_list}")