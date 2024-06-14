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

class Car:
    """
    A base class representing a car with brand and model attributes.
    """

    def __init__(self, brand, model):
        """
        Initializes the car object.

        Args:
          brand (str): The car brand.
          model (str): The car model.
        """
        self.brand = brand
        self.model = model


class Truck(Car):
    """
    A class representing a truck inheriting from Car, with additional load capacity attribute.
    """

    def __init__(self, brand, model, load_capacity):
        """
        Initializes the truck object.

        Args:
          brand (str): The truck brand.
          model (str): The truck model.
          load_capacity (float): The truck's load capacity.
        """
        super().__init__(brand, model)
        self.load_capacity = load_capacity


class PassengerCar(Car):
    """
    A class representing a passenger car inheriting from Car, with additional number of seats attribute.
    """

    def __init__(self, brand, model, num_seats):
        """
        Initializes the passenger car object.

        Args:
          brand (str): The passenger car brand.
          model (str): The passenger car model.
          num_seats (int): The number of seats in the passenger car.
        """
        super().__init__(brand, model)
        self.num_seats = num_seats


def save_trucks_in_file(cars, file_name):
    """
    Saves a list of truck objects to a file.

    Args:
      cars (list): A list of Car objects.
      file_name (str): The name of the file.
    """
    with open(file_name, "w", newline="") as file:
        for car in cars:
            # Check if car is an instance of Truck class
            if isinstance(car, Truck):
                file.write(f"{car.brand},{car.model},{car.load_capacity}\n")


cars = []
cars.append(PassengerCar("Nissan", "X-Trail", 7))
cars.append(PassengerCar("Toyota", "Yaris", 5))
cars.append(Truck("Scania", "R400", 6500))
cars.append(Truck("Iveco", "Daily", 3500))

save_trucks_in_file(cars, "./trucks.txt")
