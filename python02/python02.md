## Equality

* The `==` operator checks if two values are equal.
* It can be used with numbers, strings, and other data types.

```python
# Comparing two numbers
x = 10
y = 10

print(x == y)  # Output: True

# Comparing two strings
name1 = "John Doe"
name2 = "John Doe"

print(name1 == name2)  # Output: True
```

## Comparison operators

* Comparison operators are used to compare values.
* The available operators are `>`, `<`, `>=`, `<=`, `!=`.

```python
# Comparing two numbers
x = 10
y = 5

print(x > y)  # Output: True
print(x < y)  # Output: False

# Comparing two strings
name1 = "John Doe"
name2 = "Jane Doe"

print(name1 > name2)  # Output: False
print(name1 < name2)  # Output: True
```

##  Conditional statements

* Conditional statements allow you to execute code based on a condition being met.
* The `if` statement checks a condition and executes code if it is true.
* The `if-else` statement executes one code if the condition is true and another if it is false.
* The `elif` statement allows you to check for additional conditions in an `if` statement.

```python
# If statement
age = 18

if age >= 18:
    print("You are an adult.")

# If-else statement
number = 10

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Elif statement
grade = "A"

if grade == "A":
    print("Excellent grade!")
elif grade == "B":
    print("Very good grade!")
else:
    print("Good grade.")
```

## Logic operations (and, or, not)

* **Logical operators:**
    * Evaluate expressions involving Boolean values.
    * `and`, `or`, `not`
* **Descriptions:**
    * **AND:** Both operands must be true for the expression to be true.
    * **OR:** At least one operand must be true for the expression to be true.
    * **NOT:** Reverses the truth value of the operand.

**Examples:**

* `True and True` is True.
* `True or False` is True.
* `not False` is True.

**Code example:**

```python
# Logical AND
print(True and True)  # Output: True

# Logical OR
print(True or False)  # Output: True

# Logical NOT
print(not False)  # Output: True
```

## While loop

* A `while` loop repeatedly executes a block of code as long as a condition is true.
* An infinite loop is a `while` loop that never terminates.
* A counter variable can be used to exit a loop.

```python
# Infinite loop
while True:
    print("Hello, world!")

# Using a counter variable to exit a loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1
```

## For loop

* A `for` loop iterates over a sequence of values.
* The `range()` function generates a sequence of numbers.
* The `for` loop can be used to iterate over a string.

```python
# Iterate over a sequence of numbers
for i in range(5):
    print(i)

# Iterate over a string
for letter in "Hello, world!":
    print(letter)
```

## The break and continue statements

* The `break` statement exits a loop.
* The `continue` statement skips to the next iteration of a loop.

```python
# Using the break statement to exit a loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Using the continue statement to skip to the next iteration of a loop
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

## The loop and the else branch

* A `while` loop or `for` loop can have an `else` branch.
* The `else` branch is executed if the loop terminates normally.

```python
# While loop with an else branch
counter = 0
while counter < 5:
    print(counter)
    counter += 1
else:
    print("The loop has terminated.")

# For loop with an else branch
for i in range(5):
    print(i)
else:
    print("The loop has terminated.")
```

##  List basics

* Lists are ordered collections of data.
* They can be created using square brackets `[]`.
* Elements can be of any type, including strings, numbers, and other lists.

```python
# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Print the list
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

## Indexing and accessing elements

* Lists can be indexed using their position.
* The first element has an index of 0, the second element has an index of 1, and so on.
* Elements can be accessed using their index in square brackets.

```python
# Access the first element
first_fruit = fruits[0]  # first_fruit = "apple"

# Access the last element
last_fruit = fruits[-1]  # last_fruit = "cherry"
```

## List operations

* Lists can be added and multiplied.
* Addition of two lists concatenates them.
* Multiplication of a list by a number repeats the list that many times.

```python
# Add two lists
fruits + ["orange", "mango"]  # ['apple', 'banana', 'cherry', 'orange', 'mango']

# Multiply a list by a number
fruits * 3  # ['apple', 'banana', 'cherry', 'apple', 'banana', 'cherry', 'apple', 'banana', 'cherry']
```

## Common list methods

* Lists have several useful methods.
* `append()` adds an element to the end of the list.
* `remove()` removes an element from the list.
* `sort()` sorts the list in place.

```python
# Append an element to the list
fruits.append("mango")  # fruits = ['apple', 'banana', 'cherry', 'orange', 'mango']

# Remove an element from the list
fruits.remove("banana")  # fruits = ['apple', 'cherry', 'orange', 'mango']

# Sort the list
fruits.sort()  # fruits = ['apple', 'cherry', 'mango', 'orange']
```

## Other list features

* Lists can be nested to create 2D or even multidimensional lists.
* The `in` operator can be used to check if an element is in a list.
* The `len()` function returns the length of a list.

```python
# Nested lists
nested_list = [["apple", "banana"], ["cherry", "orange"]]

# Check if an element is in a list
"apple" in fruits  # True

# Get the length of a list
len(fruits)  # 4
```

## Looping through a list with a for loop

* The `for` loop allows you to iterate over each element in a list.
* The syntax `for i in list_name` iterates over each element and assigns it to the variable `i`.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry
```

## Slices

* Slices extract a portion of a list.
* Syntax: `list_name[start:end:step]`.
* `start` (inclusive) and `end` (exclusive) define the range of elements.
* `step` defines the increment between elements (defaults to 1).
* Negative indices can be used in slices to start from the end.

```python
fruits = ["apple", "banana", "cherry", "orange", "mango"]

# Get elements from index 1 (inclusive) to 3 (exclusive)
sliced_fruits = fruits[1:3]  # sliced_fruits = ["banana", "cherry"]

# Get elements from the second element to the end (using negative index)
sliced_fruits = fruits[1:]  # sliced_fruits = ["banana", "cherry", "orange", "mango"]

# Get every other element (step of 2)
sliced_fruits = fruits[::2]  # sliced_fruits = ["apple", "cherry", "mango"]
```

## The in and not in operators

* The `in` operator checks if a value exists in a list.
* The `not in` operator checks if a value does not exist in a list.

```python
fruits = ["apple", "banana", "cherry"]

# Check if "banana" exists in the list
"banana" in fruits  # True

# Check if "orange" does not exist in the list
"orange" not in fruits  # True
```

## Lists in lists: two-dimensional arrays

* Lists can be nested to create two-dimensional or even multidimensional lists.
* Two-dimensional lists can be used to represent tables, matrices, or other two-dimensional data structures.

```python
# 2D list representing a table
table = [
    ["Name", "Age", "City"],
    ["John Doe", 30, "New York"],
    ["Jane Doe", 25, "London"],
]

# Print the table
for row in table:
    print(row)

# Output:
# ['Name', 'Age', 'City']
# ['John Doe', 30, 'New York']
# ['Jane Doe', 25, 'London']
```

## Bit operations, Bitwise operators

* **Bitwise operators:**
    * Operate on bits of binary numbers.
    * & (AND), | (OR), ^ (XOR), ~ (NOT)
* **Descriptions:**
    * **AND:** Outputs 1 if both bits are 1, otherwise 0.
    * **OR:** Outputs 1 if at least one bit is 1, otherwise 0.
    * **XOR:** Outputs 1 if the bits are different, otherwise 0.
    * **NOT:** Flips all bits.

**Examples:**

* 1010 & 1100 = 1000 (8)
* 1010 | 1100 = 1110 (14)
* 1010 ^ 1100 = 0110 (6)
* ~1010 = 0101 (-11)

**Code example:**

```python
# Bitwise AND
print(10 & 12)  # Output: 8

# Bitwise OR
print(10 | 12)  # Output: 14

# Bitwise XOR
print(10 ^ 12)  # Output: 6

# Bitwise NOT
print(~10)  # Output: -11
```

## Deal with single bits, binary left shift and binary right shift

* **Binary left shift:**
    * Shifts the binary representation of a number to the left by a specified number of bits.
    * Multiplies by 2 raised to the power of the number of bits shifted.
* **Binary right shift:**
    * Shifts the binary representation of a number to the right by a specified number of bits.
    * Divides by 2 raised to the power of the number of bits shifted.

**Examples:**

* 1010 << 2 = 101000 (40)
* 1010 >> 2 = 10 (2)

**Code example:**

```python
# Binary left shift
print(10 << 2)  # Output: 40

# Binary right shift
print(10 >> 2)  # Output: 2
```

## Define blocks of code

In Python, indentation is used to define blocks of code. Instead of curly braces, Python uses spaces or tabs to indicate the structure of the code. This helps improve readability and organization of the code.
* It is important to use consistent indentation (4 spaces or 1 tab) throughout your code.
* Missing indentation or mixing spaces and tabs will cause a syntax error.
* PEP 8 -- Style Guide for Python Code: [https://www.python.org/dev/peps/pep-0008/](https://www.python.org/dev/peps/pep-0008/)
* Indentation is a key element of Python syntax. Understanding and using indentation is essential for writing correct and readable code.

```python
temperature = 35

if temperature > 30:
    # This block executes if the temperature is greater than 30
    print("It's hot outside!")
    print("Make sure to stay hydrated.")
elif temperature > 20:
    # This block executes if the temperature is between 20 and 30 (inclusive)
    print("It's warm outside.")
else:
    # This block executes if the temperature is 20 or below
    print("It's very cold outside!")
    print("Put on a warm jacket")
# This line is always printed regardless of the temperature
print("Have a great day!")
```



