def modify_hat_list(hat_list):
    """
    Modifies a list by replacing the middle number and removing the last element.
    """
    # Replace the middle number (assuming the list has at least 3 elements)
    if len(hat_list) >= 3:
        new_number = int(input("Enter a number to replace the middle element: "))
        hat_list[1] = new_number  # Replace the element at index 1 (middle)

    # Remove the last element
    hat_list.pop()

    # Return the modified list
    return hat_list


hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 3: Print the modified list
print(modify_hat_list(hat_list))
