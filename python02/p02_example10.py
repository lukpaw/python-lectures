# This Python program demonstrates the use of indentation to define blocks of code.

# Define the temperature
temperature = 35  # You can change this value to test different conditions

if temperature > 30:  # First if condition with two instructions
    print("It's hot outside!")  # This instruction is executed if the condition is true
    print("Make sure to stay hydrated.")  # This instruction is also executed if the condition is true
elif temperature > 20:  # Second elif condition with one instruction
    print("It's cold outside!")  # This instruction is executed if the condition is true
# The following print is not part of the elif condition above. It will be executed regardless of the condition.
# print("Have a great day!")  # This statement must be indented to be part of the elif block
else:  # Third else condition with two instructions
    print("It's very cold outside!")  # This instruction is executed if the condition is true
    print("Put on a warm jacket")  # This instruction is also executed if the condition is true
print("Have a great day!")  # This instruction is executed regardless of the condition
