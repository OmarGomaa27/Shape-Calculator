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
