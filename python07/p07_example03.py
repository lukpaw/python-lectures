import sys

# File Processing Classes
# Example: Open a text file for reading
with open("data.txt", "r") as text_file:
    # Read lines from the text file
    for line in text_file:
        print(line)

# Opening a File
# Example: Open a file for writing with UTF-8 encoding
with open("output.txt", "w", encoding="utf-8") as file:
    # Write content to the file
    file.write("This is some text data.")

# Handling File I/O Errors
try:
    with open("missing_file.txt", "r") as file:
        # This code will not execute because the file doesn't exist
        pass
except IOError as e:
    # Check the error code using the `errno` property
    if e.errno == 2:  # ENOENT: file or directory not found
        print("The file 'missing_file.txt' does not exist.")

# Predefined Streams
# Example: Read user input from standard input
print("Please enter something:")
user_input = sys.stdin.readline()
print("You entered:", user_input)
