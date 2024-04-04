def are_anagrams(str1, str2):
    """Checks if two strings are anagrams, considering case-insensitivity and ignoring spaces.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if the strings are anagrams, False otherwise.
    """

    # Remove spaces and convert to lowercase for case-insensitivity
    str1_cleaned = "".join(char.lower() for char in str1 if char.isalnum())
    str2_cleaned = "".join(char.lower() for char in str2 if char.isalnum())

    # Handle empty strings as non-anagrams
    if not str1_cleaned or not str2_cleaned:
        return False

    # Check if lengths are equal (anagrams must have the same number of characters)
    if len(str1_cleaned) != len(str2_cleaned):
        return False

    # Efficiently check for anagrams using character counts
    char_counts = {}
    for char in str1_cleaned:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in str2_cleaned:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1

    return True


# Get user input
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check for anagrams and print result
if are_anagrams(str1, str2):
    print("Anagrams")
else:
    print("Not anagrams")
