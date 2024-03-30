message = " welcome to Python "

# capitalize() - Converts first letter to uppercase
print(message.capitalize())  # Output: Welcome to Python 

# center(width, fillchar) - Centers text within a specified width
print(message.center(30, '*'))   # Output: ************welcome to Python************

# count(substring) - Counts occurrences of a substring
print(message.count('o'))       # Output: 2

# join(iterable) - Not applicable for single string

# lower() - Converts all characters to lowercase
print(message.lower())          # Output:  welcome to python 

# lstrip(chars) - Removes leading characters (default: whitespace)
print(message.lstrip())          # Output: "welcome to Python "  (Keeps trailing space)

# rstrip(chars) - Removes trailing characters (default: whitespace)
print(message.rstrip())          # Output: " welcome to Python"  (Keeps leading space)

# strip(chars) - Removes both leading and trailing characters
print(message.strip())           # Output: "welcome to Python"

# replace(old, new) - Replaces occurrences of a substring
print(message.replace("Python", "Java"))  # Output:  welcome to Java 

# rfind(substring) - Finds last occurrence of a substring (index)
print(message.rfind("Python")) # Output: 13

# split(sep=None) - Splits string into a list based on a delimiter
print(message.split())             # Output: ['welcome', 'to', 'Python']

# swapcase() - Swaps case of characters
print(message.swapcase())         # Output:  WELCOME TO pYTHON  

# title() - Capitalizes first letter of each word
print(message.title())            # Output: Welcome To Python 

# upper() - Converts all characters to uppercase
print(message.upper())            # Output:  WELCOME TO PYTHON