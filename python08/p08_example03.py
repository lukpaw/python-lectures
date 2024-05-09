def remove_vowels(word):
    """
    Removes vowels from a word and returns a list of consonants and non-vowels.
    """
    vowels = "AEIOU"
    consonants = []

    for letter in word.upper():
        if letter not in vowels:
            consonants.append(letter)
    return consonants


user_word = input("Enter your word: ")

# Remove vowels using the function and print the result
consonants_without_vowels = remove_vowels(user_word)
for consonant in consonants_without_vowels:
    print(consonant)
