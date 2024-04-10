## Iterators

* Introduced in Python to simplify looping
* An iterator is an object of a class providing at least two methods:

    * `__iter__()` - Invoked once to return the iterator itself
    * `__next__()` - Invoked to provide the next iteration's value and raises `StopIteration` when iteration ends

```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration()

# Example usage
my_iterator = MyIterator([1, 2, 3])
for item in my_iterator:
    print(item)
```

## Yield Statement

* Used only inside functions to suspend function execution
* The `yield` statement:
    * Returns the yield's argument as a result
    * Causes the function to be used as a generator (e.g., in a for loop)

```python
def generate_squares(n):
    for i in range(n):
        yield i * i

# Example usage
for sq in generate_squares(5):
    print(sq)
```

## Conditional Expressions

* An expression built using the `if-else` operator
* Evaluates to one of two expressions based on a condition

```python
age = 25
is_adult = True if age >= 18 else False
print(is_adult)  # Output: True
```

## List Comprehensions as Generators

* A list comprehension becomes a generator when used inside parentheses
* Used inside parentheses to produce a generator, inside brackets for a regular list

```python
# Generator expression
gen_expression = (el * 2 for el in range(5))
for item in gen_expression:
    print(item)  # Output: 0 2 4 6 8

# List comprehension
list_comprehension = [el * 2 for el in range(5)]
print(list_comprehension)  # Output: [0, 2, 4, 6, 8]
```

[Example 1](https://github.com/lukpaw/python-lectures/blob/main/python07/p07_example01.py)

## Lambda Functions

* Tool for creating anonymous functions (functions without a name)
* Often used for short, throwaway functions

```python
# Regular function
def square(x):
    return x * x

# Lambda function
lambda_square = lambda x: x * x

# Usage
print(square(5))  # Output: 25
print(lambda_square(5))  # Output: 25
```

## The map() Function

* Creates a copy of a list and applies a function to each element
* Returns a generator that provides the new list content element by element

```python
short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)  # Output: ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor']
```

## The filter() Function

* Creates a copy of elements from a list that satisfy a condition
* Returns a generator that provides the new list content element by element

```python
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)  # Output: ['Python', 'Monty']
```

## Closures

* A technique for storing values from an enclosing function
* Even after the enclosing function exits, the inner function can still access them

```python
def tag(tg):
    tg2 = tg  # Create a copy
    tg2 = tg[0] + '/' + tg[1:]  # Modify the copy

    def inner(str):
        return tg + str + tg2

    return inner  # Return the inner function


b_tag = tag('<b>')
print(b_tag('Monty Python'))  # Output: <b>Monty Python</b>
```

[Example 2](https://github.com/lukpaw/python-lectures/blob/main/python07/p07_example02.py)


## File Processing in Python

* Files need to be opened before use and closed afterward
* Opening a file associates it with a stream for processing data
* Three opening modes exist:
    * Read mode: only reading allowed
    * Write mode: only writing allowed
    * Update mode: both reading and writing allowed

```python
# Example: Open a file for reading
with open("data.txt", "r") as file:
    # Read content from the file
    contents = file.read()
    print(contents)
```

## File Processing Classes

* Different Python classes handle various file content types
* `BufferedIOBase`: Handles any file type
* `TextIOBase`: Specialized for text files (human-readable lines)
* Streams can be binary (any data) or text (human-readable)

```python
# Example: Open a text file for reading
with open("data.txt", "r") as text_file:
    # Read lines from the text file
    for line in text_file:
        print(line)
```

## Opening a File

* The `open()` function is used to open a file
* Syntax: `open(file_name, mode=open_mode, encoding=text_encoding)`
* Creates a stream object and associates it with the file
* Raises an exception on errors

```python
# Example: Open a file for writing with UTF-8 encoding
with open("output.txt", "w", encoding="utf-8") as file:
    # Write content to the file
    file.write("This is some text data.")
```

## Handling File I/O Errors

* `IOError` exception occurs on file operation failures
* The exception object has an `errno` property with an error code
* Use this code to diagnose the problem

```python
try:
    with open("missing_file.txt", "r") as file:
        # This code will not execute because the file doesn't exist
        pass
except IOError as e:
    # Check the error code using the `errno` property
    if e.errno == 2:  # ENOENT: file or directory not found
        print("The file 'missing_file.txt' does not exist.")
```


## Predefined Streams

* Three streams are open by default when a program starts
* `sys.stdin`: Standard input (typically keyboard)
* `sys.stdout`: Standard output (typically console)
* `sys.stderr`: Standard error output (typically console for errors)

```python
# Example: Read user input from standard input
print("Please enter something:")
user_input = sys.stdin.readline()
print("You entered:", user_input)
```

[Example 3](https://github.com/lukpaw/python-lectures/blob/main/python07/p07_example03.py)


## Reading File Contents

* Various methods available for reading file content
* `read(number)`: Reads a specified number of characters/bytes and returns them as a string
    * Can read the entire file at once if no number is provided

```python
# Example: Read the entire file
with open("data.txt", "r") as file:
    contents = file.read()
    print(contents)
```

* `readline()`: Reads a single line from the text file

```python
# Example: Read one line at a time
with open("data.txt", "r") as file:
    line = file.readline()
    print(line)
```

* `readlines(number)`: Reads a specified number of lines and returns them as a list
    * Can read all lines at once if no number is provided

```python
# Example: Read all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

* `readinto(bytearray)`: Reads bytes from the file and fills the provided bytearray

```python
# Example: Read bytes into a bytearray
with open("image1.png", "rb") as file:
    image_data = bytearray(1024)
    file.readinto(image_data)
    # Process the bytearray data
```

## Writing to a File

* Methods used to write new content into a file

* `write(string)`: Writes a string to a text file

```python
# Example: Write text to a file
with open("output.txt", "w") as file:
    file.write("This is some new text data.")
```

* `write(bytearray)`: Writes all bytes from a bytearray to a file

```python
# Example: Write bytearray data to a file
with open("image2.png", "wb") as file:
    image_data = bytearray(b" \xff\x00\x00")  # Example byte data
    file.write(image_data)
```

## Iterating over Lines

* The `open()` method returns an iterable object
* Used to iterate through all lines in a for loop

```python
# Example: Print each line of a file
with open("data.txt", "r") as file:
    for line in file:
        print(line, end='')
```

[Example 4](https://github.com/lukpaw/python-lectures/blob/main/python07/p07_example04.py)


## uname Function

* Retrieves information about the current operating system
* Returns an object with the following attributes:
    * `systemname`: Name of the operating system
    * `nodename`: Machine name on the network
    * `release`: Operating system release version
    * `version`: Operating system version
    * `machine`: Hardware identifier (e.g., x86_64)

```python
import os

# Example: Get OS information
os_info = os.uname()
print("System Name:", os_info.systemname)
print("Machine Name:", os_info.nodename)
```

## os.name Attribute

* Provides a way to identify the operating system
* Returns one of the following values:
    * `posix`: Unix-like system (e.g., Linux, macOS)
    * `nt`: Windows
    * `java`: Jython or similar Java environment

```python
import os

# Example: Check OS type
if os.name == 'posix':
    print("Running on a Unix-like system")
elif os.name == 'nt':
    print("Running on Windows")
```

## Creating Directories

* `os.mkdir()` creates a single directory
* Takes a path (relative or absolute) as an argument

```python
import os

# Example: Create a directory
try:
    os.mkdir("new_folder")
    print("Directory created successfully")
except FileExistsError:
    print("Directory already exists")
```

* `os.makedirs()` creates directories recursively

```python
# Example: Create nested directories
try:
    os.makedirs("path/to/new/directory")
    print("Directories created successfully")
except FileExistsError:
    print("Some directories already exist")
```

## Listing Directory Contents

* `os.listdir()` returns a list of files and directories
* Takes a path (optional, defaults to current working directory) as an argument
* Omits hidden entries (`.`, `..`)

```python
import os

# Example: List files and directories
directory_contents = os.listdir("data")
print("Contents:", directory_contents)
```

## Navigating Directories

* `os.chdir()` changes the current working directory
* Takes a path (relative or absolute) as an argument
* `os.getcwd()` returns the current working directory path

```python
import os

# Example: Change and get working directory
os.chdir("..")  # Move up one directory
current_dir = os.getcwd()
print("Current directory:", current_dir)
```

## Removing Directories

* `os.rmdir()` removes an empty directory

* `os.removedirs()` removes a directory and its subdirectories

```python
import os

# Example: Remove an empty directory
try:
    os.rmdir("empty_folder")
    print("Directory removed successfully")
except OSError:
    print("Directory not empty or does not exist")

# Example: Remove a directory with subdirectories (assuming it's empty)
try:
    os.removedirs("path/to/remove")
    print("Directories removed successfully")
except OSError:
    print("Directories not empty or do not exist")
```

## Executing System Commands

* `os.system()` executes a shell command as a string
* Returns the exit status of the process on Unix
* Returns the value returned by the shell after running the command on Windows

```python
import os

# Example: Create a directory using system command (careful, security risk!)
return_code = os.system("mkdir new_folder")

if return_code == 0:
    print("Directory created successfully")
else:
    print("Command failed")
```

**Note: Please make your own examples.**

## Creating a Date Object

* `date` class from `datetime` module for working with dates
* Created by passing year, month, and day arguments

```python
from datetime import date

my_date = date(2024, 4, 10)  # Today's date
print("Year:", my_date.year)
print("Month:", my_date.month)
print("Day:", my_date.day)
```

* Read-only attributes: year, month, day

## Getting Today's Date

* `today` method of the `date` class returns the current date

```python
from datetime import date

today = date.today()
print("Today:", today)
```

## Dates from Timestamps

* Unix timestamps: seconds since January 1, 1970 (UTC)
* `fromtimestamp` method to create a date object from a timestamp

```python
from datetime import date
import time

timestamp = time.time()
date_from_timestamp = date.fromtimestamp(timestamp)
print("Date from timestamp:", date_from_timestamp)
```

* `time.time()` returns the current time as a floating-point number of seconds since the epoch

## Creating Time Objects

* `time` class for working with times
* Constructor accepts optional hour, minute, second, microsecond arguments

```python
from datetime import time

specific_time = time(10, 30, 25)
print("Hour:", specific_time.hour)
print("Minute:", specific_time.minute)
print("Second:", specific_time.second)
```

## Sleeping for a Duration

* `sleep` function from the `time` module suspends execution
* Argument specifies the number of seconds to sleep

```python
import time

time.sleep(2)  # Wait for 2 seconds
print("Hello world!")
```

## Combining Dates and Times

* `datetime` class for representing both dates and times
* All arguments passed to the constructor become read-only attributes

```python
from datetime import datetime

combined_datetime = datetime(2024, 4, 10, 14, 34)
print("Datetime:", combined_datetime)
```

## Formatting Dates and Times

* `strftime` method formats a datetime object into a string
* Takes a format string with directives (e.g., `%Y` for year)

```python
from datetime import datetime

now = datetime.now()
formatted_datetime = now.strftime("%A, %B %d, %Y")  # Thursday, April 10, 2024
print(formatted_datetime)
```

## Date and Time Calculations

* Calculations supported on date and datetime objects
* Results in timedelta objects representing the difference

```python
from datetime import date

date1 = date(2025, 1, 1)
date2 = date(2024, 1, 1)

difference = date1 - date2
print(difference)  # 366 days, 0:00:00

# timedelta objects can be used in calculations (e.g., multiplied by a number)
date_in_a_year = difference * 2
print(date_in_a_year)  # 732 days, 0:00:00
```

[Example 5](https://github.com/lukpaw/python-lectures/blob/main/python07/p07_example05.py)

## Days of the Week Representation

* Days in `calendar` module range from Monday (0) to Sunday (6)

```python
import calendar

# Monday is 0, Sunday is 6
print(calendar.MONDAY)  # Output: 0
print(calendar.SUNDAY)  # Output: 6
```

## Displaying a Yearly Calendar

* `calendar.calendar(year)` displays a year's calendar

```python
import calendar

year_calendar = calendar.calendar(2025)
print(year_calendar)
```

* `calendar.prcal(year)` is an alternative that doesn't require printing

## Displaying a Monthly Calendar

* `calendar.month(year, month)` displays a specific month's calendar

```python
import calendar

month_calendar = calendar.month(2024, 10)  # October 2024
print(month_calendar)
```

* `calendar.prmonth(year, month)` is an alternative that doesn't require printing

## Changing the First Day of the Week

* `calendar.setfirstweekday(weekday)` sets the first day displayed

* Weekday argument ranges from 0 (Sunday) to 6 (Saturday)

```python
import calendar

calendar.setfirstweekday(6)  # Set Saturday as the first day
print(calendar.calendar(2024))
```

## Weekday Calculation

* `calendar.weekday(year, month, day)` gets the weekday (0-6) for a date

```python
import calendar

day_of_week = calendar.weekday(2024, 4, 10)  # Wednesday (index 3)
print(day_of_week)
```

## Week Header Customization

* `calendar.weekheader(width)` returns a formatted week header string

* `width` specifies the character width for each day (default 2, max 3)

```python
import calendar

week_header = calendar.weekheader(3)  # Maximum 3 characters per day
print(week_header)  # Output: "Mon Tue Wed Thu Fri Sat Sun"
```

## Leap Year Check

* `calendar.isleap(year)` determines if a year is a leap year

```python
import calendar

is_leap_year = calendar.isleap(2024)
print(is_leap_year)  # Output: False
```

## Custom Calendar Object

* `calendar.Calendar(firstweekday=weekday)` creates a calendar object

* `firstweekday` sets the first day displayed (optional, defaults to Monday)

```python
import calendar

custom_calendar = calendar.Calendar(6)  # Saturday as first day
for day in custom_calendar.iterweekdays():
    print(day, end=" ")  # Output: 6 0 1 2 3 4 5
```

* `iterweekdays` iterates through weekday numbers, starting with `firstweekday`.

[Example 6](https://github.com/lukpaw/python-lectures/blob/main/python07/p07_example06.py)