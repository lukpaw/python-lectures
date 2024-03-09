## Introduction

**Compilation (Java):**

* Source code (\*.java) is translated into machine code (\*.exe) once.
* Faster program execution.
* Less flexibility – every change requires recompilation.
* Lack of portability – machine code works only on a specific system.

**Interpretation (Python):**

* Source code (*.py) is interpreted line by line at runtime.
* Easier to learn and write code.
* Faster development cycle – no need for compilation.
* High portability – code works on different systems with an installed interpreter.

**Example:**

* **Java:**
    * `javac Hello.java` (compile)
    * `java Hello` (run)
* **Python:**
    * `python hello.py` (\run)

**Running Python Code:**

1. **Open the Command Prompt:** Search for "Command Prompt" or "Terminal" (depending on your operating system) and launch it.
2. **Run Python code:** Type `python` and press Enter. If you have Python installed correctly, you should see a version message followed by three greater than signs (>>>). This is the Python interpreter prompt.
3. **Execute Python statements:** Type Python code directly at the prompt and press Enter to execute it.

**Example:**

```
C:\Users\lukaszp>python  # Open the Python interpreter
>>> print("Hello")       # Python code to print "Hello"
Hello                    # Output from the code
>>>                      # The interpreter is ready for more code
```

**PyCharm:**

* IDE that makes writing Python code easier.
* Offers syntax highlighting, auto-completion, and debugging tools.

**Real-world Applications of Java:**

* **Enterprise Web Applications:** Java is widely used for developing enterprise web applications due to its scalability, security, and robustness. It is a popular choice for back-end development, with frameworks like Spring Boot making it easier to build and deploy complex applications. Java's strong support for CI/CD (Continuous Integration and Continuous Delivery) makes it a good fit for teams that need to release updates frequently and reliably.

* **Android Development:** Java is the official programming language for Android, the most popular mobile operating system in the world. This means that Java developers can build millions of apps that can be used by billions of people around the globe.

* **Big Data:** Java is a popular choice for developing big data applications due to its scalability and performance. It is used in frameworks like Hadoop and Spark for processing large amounts of data.

**Real-world Applications of Python:**

* **Machine Learning:** Python is widely used for machine learning due to its large and active community, extensive library support, and ease of use. Popular libraries like TensorFlow, PyTorch, and scikit-learn provide powerful tools for developing machine learning models.

* **Data Science:** Python is a popular choice for data science due to its flexibility and ease of use. It is used for tasks like data wrangling, analysis, and visualization. Popular libraries like NumPy, Pandas, and Matplotlib provide powerful tools for data manipulation and visualization.

* **Web Development:** Python is also used for web development, with frameworks like Django and Flask making it easy to build and deploy web applications.

**Conclusion:**

Both Java and Python are powerful and versatile programming languages with a wide range of applications. The choice of language depends on the specific needs of the project. Java is a good choice for applications that require high performance, scalability, and security. Python is a good choice for applications that require rapid development, flexibility, and ease of use.

**To sum up:**

* The choice of language depends on the needs.
* Java: compilation -> faster execution, but less flexibility.
* Python: interpretation -> easier to learn, but slower execution.

##  The print() Function

* The `print()` function is used to display output on the console.
* It can print strings, numbers, variables, and more.
* You can use the `+` operator to concatenate strings before printing.

**Example:**

```python
print("Hello, world!")
print(10 + 5)
name = "John Doe"
print(name)
```

## Literals

* Literals are raw data values in your code.
* They can be strings, numbers, Booleans, and more.
* Strings must be enclosed in quotes (single or double).
* Numbers can be integers, floats, or complex.
* Booleans are True or False values.

**Example:**

```python
"This is a string."
10  # Integer
3.14  # Float
True  # Boolean
```

## Integers

* Integers are whole numbers, positive, negative, or zero.
* Python supports other number systems besides decimal.
* Octal numbers start with `0o` and use digits 0-7.
* Hexadecimal numbers start with `0x` and use digits 0-9 and letters A-F.

**Example:**

```python
decimal = 10
octal = 0o12
hexa = 0xAF

print(decimal)  # Output: 10
print(octal)  # Output: 10 (in octal)
print(hexa)  # Output: 175 (in hexadecimal)
```

## Floats

* Floats represent numbers with decimal points.
* They are typically used for calculations involving fractions.
* Scientific notation can be used for very large or very small numbers.

**Example:**

```python
pi = 3.14159
gravity = -9.81

print(pi)  # Output: 3.14159
print(gravity)  # Output: -9.81

# Scientific notation
large_number = 1.2345e10
small_number = 1.2345e-10

print(large_number)  # Output: 1.2345e+10
print(small_number)  # Output: 1.2345e-10
```

## Ints vs. Floats

* Use integers for whole numbers.
* Use floats for numbers with decimals.
* Consider the precision and accuracy needed.
* Integers are typically faster and use less memory.

**Example:**

```python
# Integer
number_of_apples = 10

# Float
price_of_apple = 2.50

total_cost = number_of_apples * price_of_apple

print(total_cost)  # Output: 25.0
```

## Strings

* Strings are sequences of characters enclosed in quotes (single or double).
* Special characters within strings can be escaped using a backslash (`\`) followed by a code.

**Escape Characters:**

* `\n`: Newline
* `\t`: Tab
* `\\`: Backslash
* `\'`: Single quote (within single-quoted strings)
* `\"`: Double quote (within double-quoted strings)

**Example:**

```python
message1 = "Hello, world!"
message2 = 'Hello, world!'
message3 = 'student\'s task'
message4 = "student's task"
message5 = "Hello, world!\nThis is on a new line."
path = "C:\\Users\\john\\documents"

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)
print(path)
```

## Boolean Values

* Boolean values are True or False values.
* They are used in conditional statements to control the flow of a program.

**Example:**

```python
# Assigning a Boolean value to a variable
is_true = True

# Checking the value of the variable
print(is_true)  # Output: True
```

**Example:**

```python
# Checking if a user is authenticated
authenticated = False

if authenticated:
    print("Welcome, user!")
else:
    print("Please log in.")
```

## Basic Operators

* Python supports a variety of basic operators for performing mathematical operations on numbers.

**Operators:**

* `+`: Addition
* `-`: Subtraction
* `*`: Multiplication
* `/`: Division
* `//`: Integer division
* `%`: Modulus (remainder)
* `**`: Exponentiation

**Example:**

```python
# Addition
print(10 + 5)  # Output: 15

# Subtraction
print(10 - 5)  # Output: 5

# Multiplication
print(10 * 5)  # Output: 50

# Division
print(10 / 5)  # Output: 2.0

# Integer division
print(10 // 5)  # Output: 2

# Modulus
print(10 % 5)  # Output: 0

# Exponentiation
print(10 ** 2)  # Output: 100
```

##  Operators and Their Priorities

* Operators in Python have different priorities, which determine the order in which they are evaluated.
* Parentheses can be used to force an order of evaluation.

**Operator Precedence:**

1. Exponentiation
2. Multiplication and Division
3. Addition and Subtraction

**Example:**

```python
# Exponentiation is evaluated first
print(2 + 3 * 4)  # Output: 14

# Parentheses can be used to force an order of evaluation
print((2 + 3) * 4)  # Output: 20
```

## Operators and Parentheses

* Parentheses can be used to force an order of evaluation in expressions.
* This can be useful to avoid unexpected results.

**Example:**

```python
# Without parentheses, the expression is evaluated from left to right
print(2 + 3 * 4)  # Output: 14

# With parentheses, the multiplication is evaluated first
print((2 + 3) * 4)  # Output: 20
```

## Variables

* Variables are used to store data in memory.
* They can be assigned values and used in expressions.

**Naming Conventions:**

* Variable names must start with a letter or an underscore (`_`).
* They can only contain letters, numbers, and underscores.
* Variable names should be descriptive and easy to understand.

**Creating Variables:**

```python
# Create a variable named `name` and assign it the value "John Doe"
name = "John Doe"

# Create a variable named `age` and assign it the value 30
age = 30

# Create a variable named `is_student` and assign it the value True
is_student = True
```

**Using Variables:**

```python
# Print the value of the variable `name`
print(name)  # Output: John Doe

# Print the value of the variable `age`
print(age)  # Output: 30

# Print the value of the variable `is_student`
print(is_student)  # Output: True
```

**Assigning a New Value to an Existing Variable:**

```python
# Change the value of the variable `name` to "Jane Doe"
name = "Jane Doe"

# Print the new value of the variable `name`
print(name)  # Output: Jane Doe
```

## Shortcut Operators

* Shortcut operators are used to perform common operations on variables in a shorter way.

**Shortcut Operators:**

* `+=`: Addition assignment
* `-=`: Subtraction assignment
* `*=`: Multiplication assignment
* `/=`: Division assignment
* `//=`: Integer division assignment
* `%=`: Modulus assignment
* `**=`: Exponentiation assignment

**Example:**

```python
# Increase the value of the variable `x` by 1
x += 1

# Decrease the value of the variable `y` by 2
y -= 2

# Multiply the value of the variable `z` by 3
z *= 3
```

## The input() Function

* The `input()` function is used to get input from the user.
* It returns a string, which can be converted to other types.

**Example:**

```python
# Get the user's name
name = input("What is your name? ")

# Get the user's age
age = int(input("How old are you? "))

# Print the user's name and age
print("Hello, {}! You are {} years old.".format(name, age))
```

## Type Casting

* Type casting is the process of converting a value from one type to another.
* The `int()` function can be used to convert a string to an integer.
* The `float()` function can be used to convert a string to a float.

**Example:**

```python
# Convert the string "10" to an integer
number = int("10")

# Convert the string "3.14" to a float
pi = float("3.14")

# Print the value of the variable `number`
print(number)  # Output: 10

# Print the value of the variable `pi`
print(pi)  # Output: 3.14
```

## String operators

* The `+` operator can be used to concatenate strings.
* The `*` operator can be used to repeat a string a specified number of times.

**Example:**

```python
# Concatenate two strings
message = "Hello, " + "world!"

# Repeat a string 5 times
repeated_string = "abc" * 5

# Print the value of the variable `message`
print(message)  # Output: Hello, world!

# Print the value of the variable `repeated_string`
print(repeated_string)  # Output: abcabcabcabc
```

## Type conversion: str()

* The `str()` function can be used to convert a value to a string.
* This can be useful for formatting output or for storing data in a string format.

**Example:**

```python
# Convert an integer to a string
number = 10
string_number = str(number)

# Convert a float to a string
pi = 3.14
string_pi = str(pi)

# Print the value of the variable `string_number`
print(string_number)  # Output: 10

# Print the value of the variable `string_pi`
print(string_pi)  # Output: 3.14
```