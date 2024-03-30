## Object-Oriented Programming (OOP) Basics

* OOP is a programming paradigm based on the concept of "objects."
* An **object** represents a real-world entity or concept.
* A **class** is a blueprint that defines the properties (data) and behaviors (methods) of objects.

```python
class Car:  # Define a class Car
    # ... (properties and methods will be defined later)
```

## Class Hierarchies (Inheritance)

* Inheritance allows creating new classes (subclasses) based on existing classes (superclasses).
* Subclasses inherit properties and methods from their superclass.
* Inheritance relationships are shown in **inheritance diagrams**:

```
        Animal
       /     \
     Dog     Cat
```

## Properties and Methods

* Objects have a set of **properties** (data attributes) that define their state.
* Objects have a set of **methods** (functions) that define their behavior.

```python
class Dog:
    # Properties (e.g., name, breed, age)
    # Methods (e.g., bark(), play())
```

## Defining a Class in Python

* Use the `class` keyword followed by the class name.
* Indent code within the class to define its properties and methods.

```python
class MyClass:
    # Class definition here
```

## Creating Objects from a Class

* Use the class name like a function to create objects (instances).
* Each object has its own set of properties.

```python
my_object = MyClass()  # Create an object of MyClass
```

## Procedural Approach (Stack Example)

```python
stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]  # delete the last item
    return val


print(len(stack))  # Output: 0 (initial state)

push(3)
push(2)
push(1)

print(stack)  # Output: [3, 2, 1]

print(pop())  # Output: 1
print(pop())  # Output: 2
print(pop())  # Output: 3

print(stack)  # Output: []
```

[Example 1](https://github.com/lukpaw/python-lectures/blob/main/python06/p06_example01.py)

## Object-Oriented Approach (Stack Example)

```python
class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, val):
        self.stack_list.append(val)

    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        return val


# Usage
stack_object = Stack()

print(len(stack_object.stack_list))  # Output: 0 (initial state)

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.stack_list)  # Output: [3, 2, 1]

print(stack_object.pop())  # Output: 1
print(stack_object.pop())  # Output: 2
print(stack_object.pop())  # Output: 3

print(stack_object.stack_list)  # Output: []
```

[Example 2](https://github.com/lukpaw/python-lectures/blob/main/python06/p06_example02.py)

## Constructors (`__init__` method)

* The `__init__` method is a special constructor method.
* It's automatically called when you create a new object of the class.
* It's used to initialize the object's state (instance variables).
* It must have the `self` parameter.
* The constructor can have additional parameters besides `self`.
* It cannot return a value explicitly (it implicitly returns `None`).
* It cannot be called directly like a regular method.

```python
class Person:
    def __init__(self, name):  # Constructor
        self.name = name


person1 = Person("Alice")
print(person1.name)  # Output: Alice
```

## The `self` Parameter

* `self` is the first parameter of every method.
* It refers to the specific object instance the method is called on.
* Use `self` to access the object's instance and class variables.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}!")


person1 = Person("Alice")
person1.greet()  # Output: Hello, my name is Alice!
```

## OOP Properties: Instance Variables

* Instance variables are properties that belong to individual objects.
* Each object can have its own set of instance variables with different values.
* Instance variables are created and managed within the object's lifetime.
* They are stored in a special dictionary called `__dict__` within each object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age


# Create objects with different instance variables
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.name)  # Output: Alice
print(person1.age)  # Output: 30
print(person2.name)  # Output: Bob
print(person2.age)  # Output: 25

# Accessing __dict__ (not recommended for regular use)
print(person1.__dict__)  # Output: {'name': 'Alice', 'age': 30}
```

**Note:** While `__dict__` provides a way to see an object's instance variables, it's generally not recommended to access or modify it directly in your code. It's better to use public methods (getters and setters) to interact with an object's data in a controlled manner. 

## OOP Methods 

* Methods are functions defined within a class.
* They act upon the data (instance variables) of the object.
* Every method implicitly receives a parameter named `self`.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):  # Method definition
        print(f"Hello, my name is {self.name}!")


person1 = Person("Alice")
person1.greet()  # Output: Hello, my name is Alice!
person1.name = "Bob"
person1.greet()  # Output: Hello, my name is Bob!
```

## OOP Properties: Class Variables

* Class variables are shared by all instances of a class.
* There's only one copy of a class variable, and it's defined at the class level.
* Class variables are not stored in the object's `__dict__` dictionary.
* They are accessed using the class name, not the object instance.

```python
class Person:
    # Class variable to count the number of Car objects created
    num_people = 0

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
        Person.num_people += 1  # Increment class variable


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.num_people)  # Output: 2 (shared class variable)
print(Person.num_people)  # Output: 2 (access using class name)
```

## Properties: Private Instance Variables

* Instance variables can be made private by naming them with a leading double underscore (`__`).
* This convention discourages direct access from outside the class.
* However, private variables can still be accessed indirectly using a "mangled" name (`_ClassName__private_variable_name`).

```python
class Person:
    def __init__(self, name, age, money):
        self.name = name  # Instance variable
        self.age = age
        self.__money = money  # Private instance variable

    def get_money(self):  # Public method to access balance
        return self.__money


person1 = Person("Alice", 30, 200)

# Direct access is discouraged (use get_balance method)
# print(person1.__balance)  # Avoid this

print(person1.get_money())  # Output: 1000
```

## Checking Attribute Existence: hasattr()

* The `hasattr()` function checks if an object or class has a specific attribute (variable or method).
* It takes two arguments: the object/class and the attribute name (as a string).
* It returns `True` if the attribute exists, `False` otherwise.

```python
class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money

    def get_money(self):
        return self.__money


person1 = Person("Alice", 30, 200)

# Check for existing attributes
print(hasattr(person1, "name"))  # Output: True
print(hasattr(person1, "eye_color"))  # Output: False

# Check for methods
print(hasattr(person1, "get_money"))  # Output: True
print(hasattr(person1, "get_marital_status"))  # Output: False
```

[Example 3](https://github.com/lukpaw/python-lectures/blob/main/python06/p06_example03.py)

## Inner Life of Classes and Objects

* Special attributes provide information about classes and objects.

  * `__dict__`: Dictionary containing the object's instance variables (generally not for direct modification).
  * `__name__`: The class name as a string.
  * `__module__`: The module name where the class is defined (as a string).
  * `__bases__`: A tuple containing the class's parent classes (superclasses).

**Note:** These attributes are typically used internally for Python's object system and shouldn't be relied upon in everyday coding.

## Inheritance in OOP

* Inheritance allows creating new classes (subclasses) based on existing classes (superclasses).
* Subclasses inherit properties (methods and instance variables) from their superclass.
* Inheritance promotes code reusability and creates class hierarchies.

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):
        print("Woof!")


# Create objects
animal1 = Animal("Elephant")
dog1 = Dog("Labrador")

animal1.make_sound()  # Output: Generic animal sound
dog1.make_sound()  # Output: Woof!
```

## Method Overriding

* Subclasses can redefine methods inherited from the superclass.
* The new definition overrides the superclass behavior for the subclass.

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):  # Dog inherits from Animal
    def make_sound(self):
        print("Woof!")


class Cat(Animal):  # Dog inherits from Animal
    def make_sound(self):
        print("Meow!")


# Create objects
dog1 = Dog("Labrador")
cat1 = Cat("Persian")

dog1.make_sound()  # Output: Woof!
cat1.make_sound()  # Output: Meow!
```

[Example 4](https://github.com/lukpaw/python-lectures/blob/main/python06/p06_example04.py)

## Special Methods in Inheritance

* Several special methods are used with inheritance:

   * `__str__()`: Defines how an object is converted to a string (for printing, etc.).
   * `issubclass(Class1, Class2)`: Checks if `Class1` is a subclass of `Class2`.
   * `isinstance(Object, Class)`: Checks if an object belongs to a specific class.
   * `is`: Checks if two variables refer to the same object in memory.
   * `super()`: Returns a reference to the nearest superclass.

```python
class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f"Car model: {self.model}"

    # Example using issubclass (not directly related to object or instance, but demonstrates how to use it)
    def is_electric(self):
        return issubclass(self.__class__, ElectricCar)  # Check if object is subclass of ElectricCar


class ElectricCar(Car):
    def __init__(self, model, battery_range):
        super().__init__(model)  # Call superclass constructor
        self.battery_range = battery_range

    def __str__(self):
        # Override the base class __str__ to include battery range
        return f"Electric Car model: {self.model}, Battery Range: {self.battery_range}km"


# Create objects
car1 = Car("Honda Civic")
electric_car1 = ElectricCar("Tesla Model S", 400)

# Print using __str__
print(car1)  # Output: Car model: Honda Civic
print(electric_car1)  # Output: Electric Car model: Tesla Model S, Battery Range: 400km

# Example using isinstance (not directly related to object or instance, but demonstrates how to use it)
print(isinstance(electric_car1, Car))  # Output: True (ElectricCar is a subclass of Car)

# Example using is (checks object memory location, not recommended for inheritance checks)
print(car1 is car1)  # Output: True (same object)


# Example using super() to call the parent class method (can be useful for chained method calls)
class LuxuryCar(ElectricCar):
    def __init__(self, model, battery_range, features):
        super().__init__(model, battery_range)  # Call ElectricCar constructor
        self.features = features

    def get_info(self):
        # Call parent class __str__ method and add features info using super()
        return super().__str__() + f"\nFeatures: {self.features}"


luxury_car = LuxuryCar("Tesla Model X", 500, "Autopilot, Self-parking")
print(
    luxury_car.get_info())  # Output: Electric Car model: Tesla Model X, Battery Range: 500km\nFeatures: Autopilot, Self-parking
```

[Example 5](https://github.com/lukpaw/python-lectures/blob/main/python06/p06_example05.py)

## Property Resolution Order

* When searching for an object/class property (method, variable), Python follows this order:

  1. The object itself.
  2. All superclasses in the object's inheritance hierarchy (bottom to top).
  3. Left-to-right order if multiple classes exist at the same inheritance level.
  4. If not found, raises an `AttributeError` exception.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shape = Shape()
# print(shape.width)  # fails with AttributeError: 'Shape' object has no attribute 'width'
# print(shape.area())  # raise NotImplementedError

rectangle = Rectangle(4, 5)
print(rectangle.area())  # Output: 20

circle = Circle(3)
print(circle.area())  # Output: 28.26
```

[Example 6](https://github.com/lukpaw/python-lectures/blob/main/python06/p06_example06.py)

## Custom Exceptions

* Inherit from built-in exceptions to create specific error types.
* Provides more informative error messages for your application.

```python
class InsufficientFundsError(Exception):  # Inherits from Exception
    """Raised when a bank account withdrawal attempt exceeds available funds."""
    pass


class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds in your account!")
        self.balance -= amount


# Usage
try:
    account = Account(100)
    account.withdraw(150)  # Raises InsufficientFundsError
except InsufficientFundsError as e:
    print(e)  # Output: Not enough funds in your account!
```

[Example 7](https://github.com/lukpaw/python-lectures/blob/main/python06/p06_example07.py)