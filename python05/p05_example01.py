name = "Alice"
name_length = len(name)  # name_length will be 5
print(f"The name '{name}' has {name_length} characters.")

description = """This is a 
multiline string, 
demonstrating how to write 
text across several lines."""

print(description)

message = "welcome to Python"

# Concatenation (+)
greeting = "Hello, " + message  # Combines "Hello, " and "welcome to Python"
print(greeting)  # Output: Hello, welcome to Python

# Replication (*)
repeated_message = message * 3  # Repeats the string three times
print(repeated_message)  # Output: welcome to Pythonwelcome to Pythonwelcome to Python

# ord() and chr()
char_code = ord('t')  # Unicode code point for 't'
print(f"Unicode code point for 't': {char_code}")  # Output: Unicode code point for 't': 116

character = chr(80)  # Character for code point 80
print(f"Character for code point 80: {character}")  # Output: Character for code point 80: P

# min() and max()
print(f"Minimum character: {min(message)}")  # Output: Minimum character: w
print(f"Maximum character: {max(message)}")  # Output: Maximum character: y

# index()
position = message.index('o')  # Index of first 'o'
print(f"Index of first 'o': {position}")  # Output: Index of first 'o': 4

# list()
char_list = list(message)  # Converts string to a list of characters
print(char_list)  # Output: ['w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'P', 'y', 't', 'h', 'o', 'n']

# count()
letter_count = message.count('o')  # Counts occurrences of 'o'
print(f"Number of 'o' characters: {letter_count}")  # Output: Number of 'o' characters: 2
