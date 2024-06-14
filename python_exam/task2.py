"""
==========================
Task instructions:
==========================
This program calculates the sum of 5 numbers entered by the user.

==========================
Example Output:
==========================
Enter a number: 4
Enter a number: 5
Enter a number: 2
Enter a number: 6
Enter a number: 1
The sum of the 5 numbers is: 18.0
"""


def sum_of_list(numbers):
    """
    Calculates the sum of all elements in a list of numbers.

    Args:
        numbers: A list of numbers. (list)

    Returns:
        The sum of all elements in the list. (float)
    """

    # Initialize the sum to 0
    total_sum = 0

    # Loop through each element and add it to the sum
    for number in numbers:
        total_sum += number

    return total_sum


# Get user input for 5 numbers
user_list = []
while len(user_list) < 5:
    user_input = input("Enter a number: ")
    try:
        user_list.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate and print the sum
result = sum_of_list(user_list)
print("The sum of the 5 numbers is:", result)
