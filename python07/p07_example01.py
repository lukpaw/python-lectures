# Iterators
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration()


# Example usage
my_iterator = MyIterator([1, 2, 3])
for item in my_iterator:
    print(item)


# Yield Statement
def generate_squares(n):
    for i in range(n):
        yield i * i


for sq in generate_squares(5):
    print(sq)

# Conditional Expressions
age = 25
is_adult = True if age >= 18 else False
print(is_adult)  # Output: True

# List Comprehensions as Generators

# Generator expression
gen_expression = (el * 2 for el in range(5))
for item in gen_expression:
    print(item)  # Output: 0 2 4 6 8

# List comprehension
list_comprehension = [el * 2 for el in range(5)]
print(list_comprehension)  # Output: [0, 2, 4, 6, 8]
