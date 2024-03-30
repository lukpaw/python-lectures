greeting = "Hello, world!"

# Accessing characters by index
first_letter = greeting[0]  # first_letter will be 'H'
print(f"First letter: {first_letter}")

# Slicing to extract a substring
sub_string = greeting[7:12]  # sub_string will be 'world'
print(f"Sub string: {sub_string}")

sentence = "This is a Python string."

# in operator
if "Python" in sentence:
    print("'Python' is present in the sentence.")

# not in operator
if "Java" not in sentence:
    print("'Java' is not present in the sentence.")
