def mysplit(string):
    """
    Splits a string into a list of words based on whitespace.
    """

    words = []
    current_word = ""  # To build individual words
    in_word = False  # Flag to track if currently processing a word

    for char in string:
        if in_word:
            if not char.isspace():  # Check for non-whitespace character
                current_word += char
            else:  # End of word (whitespace encountered)
                words.append(current_word)
                current_word = ""  # Reset for next word
                in_word = False  # No longer in a word
        else:  # Outside a word and encountering a non-whitespace character
            if not char.isspace():
                current_word = char  # Start a new word
                in_word = True  # Now processing a word

    # Add the last word if it's not empty after the loop
    if current_word:
        words.append(current_word)

    return words


# Test cases
print(mysplit("To be or not to be, this is a question"))
print(mysplit("To be or not to be,this is a question"))
print(mysplit("  "))
print(mysplit(" abc "))
print(mysplit(""))
