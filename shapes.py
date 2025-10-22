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
    

    #   ---Circle Test---
circle = Circle("MyCircle", 5)
print(circle.area())      # 78.53975
print(circle.perimeter()) # 31.4159
print(circle)             # Circle(radius=5)