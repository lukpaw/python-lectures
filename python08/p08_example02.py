# The magician's secret number (replace with your desired number)
secret_number = 7


def play_guessing_game():
    """
    This function runs the guessing game loop and interacts with the user.
    """
    print("Guessing game! Enter your guess:")

    guess = None
    while guess != secret_number:
        try:
            guess = int(input())
        except ValueError:
            print("Invalid input! Enter an integer number: ")
            continue  # Skip to the next loop iteration if input is invalid

        if guess == secret_number:
            print("Well done, muggle! You are free now.")
        else:
            print("You're stuck in my loop! Try again: ")

    # Success message (outside the loop)
    print(f"The secret number was: {secret_number}")


# Call the guessing game function
play_guessing_game()
