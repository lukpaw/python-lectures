def calculate_reciprocals(num_values):
    """
    Calculates and prints the reciprocals of a given number of natural numbers.
    """

    for i in range(num_values):
        try:
            value = int(input(f"Enter natural number {i + 1}: "))
            reciprocal = 1 / value
            print(f"The reciprocal of {value} is {reciprocal}")
        except ValueError:
            print("Invalid input! Please enter an integer.")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")


# Set the number of values to read
num_values = 5
calculate_reciprocals(num_values)
