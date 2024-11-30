import math
from functools import reduce

from .base import Polygon


class Circle(Polygon):
    
    def __init__(self, *dimensions) -> None:
        
        class_name: str = self.__class__.__name__
        
        super().__init__(class_name, 1, *dimensions)
        
    def compute_area(self) -> float:
        radius: float = self.dimensions[0]
        return math.pi * radius ** 2
        
    def compute_perimeter(self) -> float:
        radius: float = self.dimensions[0]
        return 2 * math.pi * radius
    

class Triangle(Polygon):
    
    def __init__(self, *dimensions) -> None:
        class_name: str = self.__class__.__name__
        super().__init__(class_name, 3, *dimensions)
    
    def compute_area(self) -> float:        
        # Heron's formula
        dimensions = self.dimensions
        s: float = sum(dimensions) / 2  # Semiperimeter
        return math.sqrt(s * (s - dimensions[0]) * (s - dimensions[1]) * (s - dimensions[2]))
        
    def compute_perimeter(self) -> float:
        
        return sum(self.dimensions)
    
    
class Rectangle(Polygon):
    
    def __init__(self, *dimensions) -> None:
        class_name: str = self.__class__.__name__
        super().__init__(class_name, 4, *dimensions)

    def compute_area(self) -> float:
        return reduce(lambda x, y: x * y, self.dimensions[:2])
        
    def compute_perimeter(self) -> float:
        return 2 * sum(self.dimensions[:2])


class RegularPolygon(Polygon):
    
    def __init__(self, *dimensions) -> None:
        class_name: str = self.__class__.__name__
        super().__init__(class_name, len(dimensions)-1, *dimensions)
        self.number_sides: int = len(self.dimensions)
        self.side_length: float = self.dimensions[0]
    
    def compute_area(self) -> float:
        apothem: float = self.side_length / (2 * math.tan(math.pi / self.number_sides))
        return (self.compute_perimeter() * apothem) / 2
        
    def compute_perimeter(self) -> float:
        return self.side_length * self.number_sides