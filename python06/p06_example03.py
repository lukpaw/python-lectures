class Person:
    num_people = 0

    def __init__(self, name, age=None, money=None):
        self.name = name
        self.age = age
        self.__money = money
        Person.num_people += 1

    def get_age(self):
        return self.age

    def get_money(self):
        return self.__money

    def greet(self):
        print(f"Hello, my name is {self.name}!")


person0 = Person("John")
print(person0.name)

person1 = Person("Alice", 30, 200)
person2 = Person("Bob", 25, 300)

print(f"{person1.name} is {person1.age} years old")
print(f"{person2.name} is {person2.age} years old")

# Accessing __dict__ (not recommended for regular use)
print(person1.__dict__)

# Direct access is discouraged (use get_balance method)
# print(person1.__balance)  # Avoid this

print(person1.get_money())

print("num people")
print(person1.num_people)
print(Person.num_people)

# Check for existing attributes
print(hasattr(person1, "name"))
print(hasattr(person1, "eye_color"))

# Check for methods
print(hasattr(person1, "get_money"))
print(hasattr(person1, "get_marital_status"))

person1 = Person("Alice", 30, 200)
person1.greet()
person1.name = "Bob"
person1.greet()
