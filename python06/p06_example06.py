class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


shape = Shape()
# print(shape.width)  # fails with AttributeError: 'Shape' object has no attribute 'width'
# print(shape.area())  # raise NotImplementedError

rectangle = Rectangle(4, 5)
print(rectangle.area())  # Output: 20

circle = Circle(3)
print(circle.area())  # Output: 28.26
