import math

class Shape:
    """Base class for all shapes."""
    
    def __init__(self, name):
        self.name = name
    
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("Subclass must implement area()")
    
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        raise NotImplementedError("Subclass must implement perimeter()")
    
    def __str__(self):
        return f"{self.name}"


class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


# ---Circle Test---
circle = Circle("MyCircle", 5)
print(circle.area())      # 78.53975
print(circle.perimeter()) # 31.4159
print(circle)             # Circle(radius=5)


class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# ---Rectangle Test---
rect = Rectangle("MyRect", 4, 6)
print(rect.area())      # 24
print(rect.perimeter()) # 20
print(rect)             # Rectangle(width=4, height=6)


class Triangle(Shape):
    """Class representing a triangle."""

    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Triangle(sides={self.side1},{self.side2},{self.side3})"


# ---Triangle Test---
triangle = Triangle("MyTriangle", 3, 4, 5)
print(triangle.area())      # 6.0
print(triangle.perimeter()) # 12
print(triangle)             # Triangle(sides=3,4,5)


class ShapeCollection:
    """Manages a collection of shapes."""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """Add a shape to the collection."""
        self.shapes.append(shape)

    def total_area(self):
        """Return the sum of all shapes' areas."""
        return sum(shape.area() for shape in self.shapes)

    def total_perimeter(self):
        """Return the sum of all shapes' perimeters."""
        return sum(shape.perimeter() for shape in self.shapes)


# ---ShapeCollection Test---
collection = ShapeCollection()
collection.add_shape(Circle("C1", 5))
collection.add_shape(Rectangle("R1", 4, 6))
print(collection.total_area())      # 102.53975
print(collection.total_perimeter()) # 51.4159
