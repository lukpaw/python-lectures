def find_largest_number(numbers):
    """
    Finds the largest number in a list of numbers.
    """
    if not numbers:
        return None  # Handle empty list case

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def get_numbers_from_user():
    """
    Prompts the user to enter 5 numbers and returns them as a list.
    """
    numbers = []
    for i in range(5):
        number = int(input(f"Enter number {i + 1}: "))
        numbers.append(number)
    return numbers


# Get numbers from user
numbers = get_numbers_from_user()

# Find the largest number
largest = find_largest_number(numbers)

if largest is not None:  # Check if list is not empty
    print("The largest number is:", largest)
else:
    print("No numbers were entered.")
