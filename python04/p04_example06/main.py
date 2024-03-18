import sys
sys.path.append('./modules')  # Add the modules directory to the search path

from my_package.my_functions import calculate_area

area = calculate_area(5, 3)
print(f"Area of rectangle: {area}")