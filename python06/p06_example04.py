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
animal1 = Animal("Elephant")
dog1 = Dog("Labrador")
cat1 = Cat("Persian")

animal1.make_sound()  # Output: Generic animal sound
dog1.make_sound()  # Output: Woof!
cat1.make_sound()  # Output: Meow!
