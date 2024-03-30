## UTF-8 - Character Encoding

* **Dominant in the Web World:**  UTF-8 is the most widely used character encoding for electronic communication, especially the web. 
* **Smart and Efficient:**  It uses a variable-length approach, assigning the minimum number of bits (1 to 4 bytes) to represent each character. 
* **Flexibility for All Languages:**  This allows UTF-8 to handle a vast range of characters, from basic Latin letters (8 bits) to complex ideographs (24 bits).
* **BOM (Byte Order Mark):**  An optional feature that signals the presence of UTF-8 encoding in a file.

**Examples:**

* English letters (a-z, A-Z) - 8 bits
* National characters (ą, ń, ę) - 16 bits
* Chinese characters - 24 bits

## Python I18N

* **Internationalization Made Easy (I18N):**  Python seamlessly integrates with UTF-8, enabling you to:
    * Use Unicode characters freely in variable names, strings, and other elements.
    * Process input and output that includes characters from various languages.
* **Truly Global Support:**  This built-in Unicode support makes Python an ideal choice for developing internationalized applications.

## Strings in Python

* Essential building blocks for text data
* Represent sequences of characters
* Immutable: Once created, their content cannot be changed
* `len()` function determines the number of characters in a string
* Returns an integer value

```python
name = "Alice"
name_length = len(name)  # name_length will be 5
print(f"The name '{name}' has {name_length} characters.")
```

## Multiline Strings

* Create strings spanning multiple lines using triple quotes (''' or """)
* Useful for long text or formatted code

```python
description = """This is a 
multiline string, 
demonstrating how to write 
text across several lines."""

print(description)
```

## String Operations

* **Concatenation (+):** Joins two strings
* **Replication (*):** Creates a new string by repeating a string a specific number of times
* **ord()**: Returns the Unicode code point for a given character
* **chr()**: Converts a Unicode code point to its corresponding character
* **min() & max()**: Find the minimum and maximum characters (based on Unicode order)
* **index()**: Locates the first occurrence of a substring within a string
* **list()**: Converts a string to a list of characters
* **count()**: Counts the number of occurrences of a substring within a string

```python
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
```

[Example 1](https://github.com/lukpaw/python-lectures/blob/main/python05/p05_example01.py)

## Strings as Sequences: Indexing & Slicing

* Strings are ordered sequences, characters can be accessed by index (starting from 0)
* Slicing extracts a portion of the string using start:end:step syntax

```python
greeting = "Hello, world!"

# Accessing characters by index
first_letter = greeting[0]  # first_letter will be 'H'
print(f"First letter: {first_letter}")

# Slicing to extract a substring
sub_string = greeting[7:12]  # sub_string will be 'world'
print(f"Sub string: {sub_string}")
```

## Operators: in and not in 

* `in`: Checks if a substring is present within a string (returns True/False)
* `not in`: Checks if a substring is not present within a string (returns True/False)

```python
sentence = "This is a Python string."

# in operator
if "Python" in sentence:
    print("'Python' is present in the sentence.")

# not in operator
if "Java" not in sentence:
    print("'Java' is not present in the sentence.")
```

[Example 2](https://github.com/lukpaw/python-lectures/blob/main/python05/p05_example02.py)

## String Methods

* Built-in functions that perform various operations on strings
* Some commonly used methods:
    * `capitalize()`: Converts the first letter to uppercase
    * `center()`: Pads a string to a certain width with a specified fill character
    * `count()`: Counts the number of occurrences of a substring
    * `join()`: Joins elements of an iterable (like a list) into a string
    * `lower()`: Converts all characters to lowercase
    * `lstrip()`: Removes leading whitespaces
    * `replace()`: Replaces occurrences of a substring with another substring
    * `rfind()`: Finds the last occurrence of a substring
    * `rstrip()`: Removes trailing whitespaces
    * `split()`: Splits a string into a list based on a delimiter
    * `strip()`: Removes both leading and trailing whitespaces
    * `swapcase()`: Swaps the case of characters (uppercase to lowercase and vice versa)
    * `title()`: Converts the first letter of each word to uppercase
    * `upper()`: Converts all characters to uppercase

```python
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
```

[Example 3](https://github.com/lukpaw/python-lectures/blob/main/python05/p05_example03.py)

## Comparing Strings

* Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) can be used to compare strings

```python
word1 = "apple"
word2 = "banana"

# Equal comparison
if word1 == word2:
    print(f"{word1} and {word2} are equal.")
else:
    print(f"{word1} and {word2} are not equal.")

# Less than comparison
if word1 < word2:
    print(f"{word1} is alphabetically before {word2}.")
else:
    print(f"{word1} is alphabetically after {word2}.")
```

## Sorting Strings

* Built-in `sorted()` function can be used to sort strings alphabetically
* Optionally, reverse order can be specified using `reverse=True`

```python
fruits = ["banana", "apple", "cherry"]
print(f"Fruits: {fruits}")

sorted_fruits = sorted(fruits)  # sorted_fruits will be ['apple', 'banana', 'cherry']
print(f"Sorted fruits: {sorted_fruits}")

reversed_fruits = sorted(fruits, reverse=True)  # reversed_fruits will be ['cherry', 'banana', 'apple']
print(f"Reversed fruits: {reversed_fruits}")
```

[Example 4](https://github.com/lukpaw/python-lectures/blob/main/python05/p05_example04.py)

## Strings vs. Numbers in Python

* Strings represent textual data (sequences of characters)
* Numbers represent numeric values (integers or floating-point)
* `str()`: Converts numbers to strings
* `int()`: Converts strings (representing integers) to integers
* `float()`: Converts strings (representing floating-point numbers) to floats

```python
num = 42
string_num = str(num)  # string_num will be "42"
print("String num: " + string_num)

float_num = 3.14
string_float = str(float_num)  # string_float will be "3.14"
print("String float: " + string_float)

pi_string = "3.14159"
pi_float = float(pi_string)  # pi_float will be 3.14159
# print("Pi float: " + pi_float)
# print("Pi float: " + str(pi_float))
print(f"Pi float: {pi_float}")

value = "123"
# int_value = int(value)  # This will work if value is a valid integer
int_value = int(value)  # Assuming value always contains a valid integer
print(f"Int float: {int_value}")
```

[Example 5](https://github.com/lukpaw/python-lectures/blob/main/python05/p05_example05.py)

**Note:** `int()` and `float()` can raise a `ValueError` if the conversion fails (e.g., trying to convert a non-numeric string).

## Errors, Exceptions

* Errors: unexpected problems that halt program execution (e.g., syntax errors)
* Exceptions: controlled runtime errors that can be handled using `try-except` blocks

**Using try-except for Exception Handling**

* `try` block: code that might raise an exception
* `except` block: code to handle the exception if it occurs

```python
try:
    user_age = int(input("Enter your age: "))
    print(f"You are {user_age} years old.")
except ValueError:
    print("Invalid input. Please enter a number.")
```

## Assertions

* Assertions are debugging statements used to verify assumptions about code
* The `assert` statement raises an `AssertionError` if the condition fails

```python
name = input("Enter your name: ")
assert len(name) > 0, "Name cannot be empty"  # Raises AssertionError if name is empty
print(f"Your name is {name}.")
```

[Example 6](https://github.com/lukpaw/python-lectures/blob/main/python05/p05_example06.py)

## Built-in Python Exception categories
**Abstract Exceptions (Base Classes):** Represent general exception categories (not usually raised directly). Examples:
  * `ArithmeticError`: Raised for errors in arithmetic operations (e.g., division by zero).
  * `BaseException`: The root of all exceptions in Python.
  * `LookupError`: Raised when a lookup operation fails (e.g., accessing a non-existent key in a dictionary).

**Concrete Exceptions:** Represent specific error conditions during program execution. Examples:
  * `AssertionError`: Raised when an `assert` statement fails.
  * `ImportError`: Raised when a module cannot be imported.
  * `IndexError`: Raised when an index is outside the bounds of a sequence.
  * `KeyboardInterrupt`: Raised when the user interrupts the program with Ctrl+C.
  * `KeyError`: Raised when a key is not found in a dictionary.
  * `MemoryError`: Raised when there is not enough memory available.
  * `OverflowError`: Raised when an operation overflows (e.g., calculation results in a number too large).

```python
# Example for ArithmeticError (division by zero)
# We wrap this in a try-except block to handle the exception gracefully
try:
    result = 10 / 0
except ZeroDivisionError as e:  # We catch the specific ArithmeticError subclass
    print(f"Error: {e}")  # Print the error message
else:
    print(f"Result (should not print): {result}")  # This won't execute due to exception

# IndexError: accessing an index outside the list bounds
my_list = [1, 2, 3]
try:
    value = my_list[4]  # Index 4 is out of range
except IndexError as e:
    print(f"Index error: {e}")

# KeyError: accessing a non-existent key in a dictionary
my_dict = {"name": "Alice", "age": 30}
try:
    age = my_dict["city"]  # Key "city" doesn't exist
except KeyError as e:
    print(f"Key error: {e}")
```

[Example 7](https://github.com/lukpaw/python-lectures/blob/main/python05/p05_example07.py)