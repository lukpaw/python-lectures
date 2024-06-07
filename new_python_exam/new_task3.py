"""
==========================
Task instructions:
==========================
This program defines three classes using inheritance for a simple calculator:
  - Operation: A base class representing a generic calculator operation.
      - Fields: num1, num2 (numbers to operate on).
      - Method: make_operation() - Defines the interface for performing an operation on num1 and num2.

  - Addition: A derived class inheriting from Operation, specifically for addition.
      - Method: make_operation() (overrides base class method) - Performs addition and returns the result.

  - Subtraction: A derived class inheriting from Operation, specifically for subtraction.
      - Method: make_operation() (overrides base class method) - Performs subtraction and returns the result.

==========================
Usage:
==========================
print("Addition:")
add_operation = Addition(5, 3)
result = add_operation.make_operation()
print(f"{add_operation.num1} + {add_operation.num2} = {result}")

print("\nSubtraction:")
sub_operation = Subtraction(10, 4)
result = sub_operation.make_operation()
print(f"{sub_operation.num1} - {sub_operation.num2} = {result}")

==========================
Example Output:
==========================
Addition:
5 + 3 = 8

Subtraction:
10 - 4 = 6
"""