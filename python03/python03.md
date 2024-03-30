## Why are functions used?

* Code reuse: Same instructions needed in multiple places.
* Reduced Duplication: Avoid copying and pasting code.
* Improved Readability: Code is broken into smaller, well-defined functions.
* Encapsulation: Functions isolate specific tasks.
* Maintainability: Easier to modify and update code.

## Where do functions come from?

* **Built-in functions:** Provided by Python itself (e.g. `print()`).
* **Pre-installed modules:** Available in pre-installed Python modules (require importing).
* **User-defined functions:** Written by the programmer for specific tasks.

## Defining a function

```python
# parameters are optional
def function_name(parameter1, parameter2="default value"):
    # the body of the function
```

Functions are defined using the `def` keyword followed by specific rules:

* **`def` keyword:** Signals the start of a function definition.
* **Function name:** Follows the `def` keyword and adheres to variable naming conventions.
* **Parameters (optional):** Enclosed in parentheses after the function name. Represent variables used within the function.
    * **Scope:** Exist only within the function's definition.
    * **Assignment:** Values are assigned during function calls using arguments.
      * **Default values:** Parameters can have default values assigned in the function definition. These values are used if no argument is provided during the function call.
* **Colon:** Marks the end of the function header.
* **Function body:** Indented block containing the function's logic.
    * **Execution:** Executes when the function is called.
    * **Nesting:** Indentation defines the function's scope.

```python
def introduction(first_name, last_name="Anonymous", age=-1):
    print(f"Hello, my name is {first_name} {last_name}")
    if age >= 0:
        print(f"I am {age} years old.")
```

## Calling a function

### Positional parameter passing
```python
introduction("Luke", "Skywalker", 25)
```

### Keyword argument passing
```python
introduction(first_name="James", last_name="Bond", age=45)
introduction(last_name="Skywalker", first_name="Luke", age=25)
```

### Mixing positional and keyword arguments
```python
introduction("Luke", age=25, last_name="Skywalker")
```

### Default values 
```python
introduction("James")
```

**Important:**
* Parameters exist only inside functions in which they have been defined
* Assigning a value to the parameter is done at the time of the function's invocation
* Parameters live inside functions
* Arguments exist outside functions

## The `return` Instruction

The `return` instruction is used within functions to control their execution and provide output.

* **`return` without expression:**
    * Immediately terminates the function.
    * Optional for functions without a specific result to return.
    * Example:

    ```python
    def greet(name="Anonymous"):
        print("Hello")
        if name == "Anonymous":
            return  # Optional return here
        print(f" {name}")
        return  # Optional return here
    ```

* **`return` with expression:**
    * Immediately terminates the function.
    * Evaluates the expression and returns its value as the function's result.
    * Required for functions that must return a value.
    * Example:

    ```python
    def add(x, y):
        return x + y

    result = add(5, 3)  # result will be 8
    ```

* **Ignoring the Return Value:**
    * Permissible to ignore the function's return value if the function's side effects (actions it performs) are desired.
* **Mandatory Return Values:**
    * Functions intended to return a value must use the `return` with expression variant.

## The `None` Keyword

In Python, `None` represents the absence of a value. It's a special data type with specific use cases:

* **Assigning to Variables:** Used to indicate a variable doesn't hold a value yet.

```python
value = None
```

* **Function Return Values:** Functions can return `None` to signal they don't have a specific result.

* **Checking Variable State:** The `is` operator is used to compare a variable against `None` to determine if it has a value assigned.

```python
if value is None:
    print("Sorry, you don't carry any value")
```

**Important:**

* `None` is not the same as 0, an empty string, or `False`. 
* Use `is` for exact comparison with `None`, not `==`.

## Functions with Lists

Functions can process and manipulate lists as input and output.

**Example: Square a List**

This function takes a list of numbers (`numbers`) and returns a new list with each number squared.

```python
def square_list(numbers):
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number * number)
    return squared_numbers

data = [1, 2, 3, 4]
squared_data = square_list(data)
print(squared_data)  # Output: [1, 4, 9, 16]
```

## Functions, Scopes, and the Global Keyword

In Python, functions and variables have specific scopes that define their accessibility.

* **Local Scope:** Variables defined within a function are only accessible within that function.

```python
name = "Global Alice"  # Global variable

def greet():
    name = "Local Bob"  # Local variable
    print(f"Hello, {name}!")  # Accesses local name

print(f"Before function: {name}")  # Accesses global name
greet()  # Output: Hello, Local Bob!
print(f"After function: {name}")  # Still accesses global name
```

* **Global Scope:** Variables defined outside of all functions are globally accessible.

```python
message = "Hello"  # Global variable

def say_something():
    print(message)

say_something()  # Output: Hello
```

* **Global Keyword:** The `global` keyword allows modifying a global variable from within a function.

```python
count = 0

def increment():
    global count  # Declare modifying a global variable
    count += 1
    print(count)

increment()  # Output: 1
increment()  # Output: 2

print(count)  # Output: 2 (global count is modified)
```

**Use Global Carefully:** Excessive use of `global` can make code harder to understand and maintain. It's generally recommended to limit global variable usage and favor passing data as arguments to functions.

## Tuples vs. Lists

Tuples and lists are fundamental data structures in Python, but they have distinct characteristics:

* **Mutability:**
    * **Lists:** Mutable - elements can be changed after creation.
    * **Tuples:** Immutable - elements cannot be modified after creation.
* **Ordering:**
    * **Both:** Ordered collections of elements. Elements are accessed by index.

**Example (Numbers):**

```python
# Mutable list
numbers = [1, 2, 3]
numbers[1] = 5  # Modify the second element

# Immutable tuple
numbers_tuple = (1, 2, 3)
# numbers_tuple[1] = 5  # This will cause an error (tuples are immutable)
```

**Use Cases:**

* **Lists:** When you need a collection that can be changed (e.g., shopping lists, dynamic data sets).
* **Tuples:** When you need a fixed data set that cannot be accidentally modified (e.g., coordinates, configuration values).


## Dictionaries

Dictionaries are another essential data structure in Python for storing collections of key-value pairs.

* **Unordered:** Elements are not stored in a specific sequence.
* **Keys:** Unique and immutable (used for accessing values).
* **Values:** Can be of any data type.

**Example (Contact Information):**

```python
# Create a dictionary
contact = {
    "name": "Alice",
    "phone": "123-456-7890",
    "email": "alice@example.com"
}

# Access values using keys
name = contact["name"]
phone = contact["phone"]

# Add new key-value pair
contact["city"] = "New York"
```

**Use Cases:**

* Storing configuration settings.
* Representing real-world entities with attributes (e.g., user profiles, product data).

## Operations on Tuples and Lists

While both tuples and lists share some functionality, their immutability leads to differences in available operations.

* **Common Operations:**
    * **Indexing and Slicing:** Accessing elements by position or range (same for both).
    * **Membership Testing:** Checking if an element exists in the collection (same for both).
    * **Length:** Determining the number of elements (same for both).

**Example (Accessing Elements):**

```python
numbers_list = [1, 2, 3, 4]
numbers_tuple = (1, 2, 3, 4)

first_element_list = numbers_list[0]  # Accesses the first element
first_element_tuple = numbers_tuple[0]

# Slicing to get a sub-list or sub-tuple
sub_list = numbers_list[1:3]  # Get elements from index 1 (inclusive) to 3 (exclusive)
sub_tuple = numbers_tuple[1:3]
```

* **List-Specific Operations:**
    * **Modification:** Elements can be added, removed, or changed (not applicable to tuples).
    * **Sorting:** Lists can be reordered based on a specific criteria (not applicable to tuples).

```python
numbers_list.append(5)  # Add an element to the list
numbers_list.remove(2)  # Remove an element from the list
numbers_list.sort()      # Sort the list in ascending order
```

## Operations on Dictionaries

Dictionaries provide unique operations for working with key-value pairs.

* **Adding Key-Value Pairs:** Assigning a value to a new key creates a new entry.

```python
contact = {}
contact["name"] = "Bob"
contact["email"] = "bob@example.com"
```

* **Accessing Values by Key:** Use the key to retrieve the associated value.

```python
phone_number = contact["phone"]  # Get the value associated with the "phone" key
```

* **Modifying Values:** Change the value associated with an existing key.

```python
contact["email"] = "new_email@example.com"
```

* **Checking Key Existence:** Use the `in` operator to see if a key exists in the dictionary.

```python
if "city" in contact:
    print("City information is available")
else:
    print("City information is missing")
```

* **Removing Key-Value Pairs:** Use the `del` keyword to remove a key-value pair.

```python
del contact["email"]
```

Here's the revised slide with the second example using a built-in exception:

## Exceptions

Exceptions are mechanisms for handling unexpected errors that occur during program execution. They allow the program to gracefully exit or recover from these errors.

* **Types of Exceptions:**
    * **Built-in exceptions:** Provided by Python (e.g., `IndexError`, `ZeroDivisionError`).
    * **User-defined exceptions:** Created by the programmer using the `Exception` class.

* **Exception Handling Flow:**
    1. **`try` block:** Contains code that might raise an exception.
    2. **`except` block (optional):** Catches specific exceptions and provides alternative behavior.
        * Can handle multiple exception types using a comma-separated list or the general `Exception` class.
    3. **`else` block (optional):** Executes if no exception occurs within the `try` block.
    4. **`finally` block (optional):** Always executes, regardless of exceptions. Often used for cleanup tasks.

**Example (Division by Zero):**

```python
def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("Sorry, you cannot divide by zero!")
  else:
    print(f"Result: {result}")

divide(10, 2)  # Output: Result: 5.0
divide(10, 0)  # Output: Sorry, you cannot divide by zero!
```

**Example (Using Built-in Exception):**

```python
def verify_age(age):
  try:
    if age < 18:
      raise ValueError("Age must be 18 or older.")  # Use built-in ValueError
    print(f"You are old enough.")
  except ValueError as e:
    print(e)  # Print the error message

verify_age(25)  # Output: You are old enough.
verify_age(15)  # Output: Age must be 18 or older.
```

* **Key Points:**
    * The first example remains the same, demonstrating handling a built-in exception.
    * The second example now uses the built-in `ValueError` exception to indicate an invalid age. 
    * The `except` block can handle the `ValueError` and print its message.
