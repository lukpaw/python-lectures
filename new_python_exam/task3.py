"""
==========================
Task Instructions:
==========================

This program defines class hierarchies for cars and demonstrates saving truck data to a file.

Classes:
- Car (Base Class):
    - Represents a generic car with attributes:
        - brand (str): The car brand.
        - model (str): The car model.
- Truck (Child Class):
    - Inherits from Car and adds an attribute:
        - load_capacity (float): The truck's load capacity in tons.
- PassengerCar:
    - Inherit from Car and add an attribute:
        - num_seats (int): The number of seats in the passenger car.

Functions:
- save_trucks_in_file(cars, file_name):
    - Saves a list of Truck objects to a file.
        - Args:
            - cars (list): A list of Car objects (will only save Truck instances).
            - file_name (str): The name of the file.

==========================
Usage:
==========================
cars = []
cars.append(PassengerCar("Nissan", "X-Trail", 7))
cars.append(PassengerCar("Toyota", "Yaris", 5))
cars.append(Truck("Scania", "R400", 6500))
cars.append(Truck("Iveco", "Daily", 3500))

save_trucks_in_file(cars, "./trucks.txt")

==========================
Example Output (./trucks.txt):
==========================
Scania,R400,6500.0
Iveco,Daily,3500.0
"""