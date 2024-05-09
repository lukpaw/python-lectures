def find_element_index(my_list, target):
    """
    Finds the index of a given element in a list.
    """
    for i in range(len(my_list)):
        if my_list[i] == target:
            return i
    return -1  # Not found


# Get the number to find from the user
try:
    to_find = int(input("Enter the number to find: "))
except ValueError:
    print("Invalid input! Please enter an integer number.")
    exit()  # Exit the program if input is not an integer

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = find_element_index(my_list, to_find)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")
