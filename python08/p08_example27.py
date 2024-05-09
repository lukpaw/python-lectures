class Shape:
    def area(self):
        return "Shape area (maybe unknown). "
        # raise NotImplementedError("Subclasses should implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return super().area() + "Rectangle area: " + str(self.width * self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return "Circle area: " + str(3.14 * self.radius ** 2)


def print_area(shape: Shape):
    print("shape.area(): " + str(shape.area()))


shape1 = Shape()
print_area(shape1)

rectangle = Rectangle(4, 5)
print_area(rectangle)

circle = Circle(3)
print_area(circle)