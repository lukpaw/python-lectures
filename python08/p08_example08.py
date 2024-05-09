def count_lottery_hits(bets, drawn):
    """
    Calculates the number of hits between two lottery number lists.
    """
    hits = 0
    for number in bets:
        if number in drawn:
            hits += 1
    return hits


def get_lottery_numbers():
    """
    Prompts the user to enter a specific number of lottery numbers and returns them as a list.
    """
    numbers = []
    for i in range(6):
        number = int(input(f"Enter lottery bet {i + 1}: "))
        numbers.append(number)
    return numbers


# Get drawn numbers
drawn = [5, 11, 9, 42, 3, 49]

# Get user's bets (assuming 6 numbers)
bets = get_lottery_numbers()

hits = count_lottery_hits(bets, drawn)

print(f"You hit {hits} numbers!")
