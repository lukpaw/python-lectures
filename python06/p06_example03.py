class Person:
    num_people = 0

    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.__money = money
        Person.num_people += 1

    def get_money(self):
        return self.__money

    def greet(self):
        print(f"Hello, my name is {self.name}!")


person1 = Person("Alice", 30, 200)
person2 = Person("Bob", 25, 300)

print(person1.name)
print(person2.age)

# Accessing __dict__ (not recommended for regular use)
print(person1.__dict__)

# Direct access is discouraged (use get_balance method)
# print(person1.__balance)  # Avoid this

print(person1.get_money())

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
