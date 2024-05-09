def get_unique_numbers():
    """
    Prompts user for 5 numbers, removes duplicates, and returns a list of unique numbers.
    """
    my_list = []
    num_count = 0

    while num_count < 5:
        # Get user input for numbers
        user_input = input(f"Enter number {num_count + 1}: ")
        try:
            # Convert input to a number (integer)
            number = int(user_input)
            # Add number to the list
            my_list.append(number)
            num_count += 1  # Increment counter after successful input
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Remove duplicate elements and convert the list to a set for efficient lookups
    unique_numbers = set(my_list)

    # Print the unique elements
    print("The list with unique elements only:")
    print(unique_numbers)


# Call the function to get unique numbers
get_unique_numbers()
