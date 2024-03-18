import math
import os as operating_system


# Calculate the hypotenuse of a right triangle using Pythagorean theorem
def calculate_hypotenuse(l1, l2):
    return math.sqrt(l1 ** 2 + l2 ** 2)


# Example usage:
leg1 = 5
leg2 = 12
hypotenuse = calculate_hypotenuse(leg1, leg2)

print(f"The hypotenuse of a right triangle with legs {leg1} and {leg2} is: {hypotenuse:.2f}")


# Calculate the area of a circle using the pi constant
def calculate_circle_area(r):
    return math.pi * r ** 2


# Example usage:
radius = 3
circle_area = calculate_circle_area(radius)

print(f"The area of a circle with radius {radius} is: {circle_area:.2f}")


# Get the current working directory using the renamed function
current_dir = operating_system.getcwd()

print(f"Current working directory: {current_dir}")