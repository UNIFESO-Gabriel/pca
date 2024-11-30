from enum import Enum
from abc import ABC, abstractmethod
from ..utils import validators


class ShapeType(Enum):
    CIRCLE = "circle"
    RECTANGLE = "rectangle"
    TRIANGLE = "triangle"
    POLYGON = "polygon"


class Polygon(ABC):
    
    def __init__(self, class_name: str, expected_quantity: int, *dimensions) -> None:
        self.expected_quantity: int = expected_quantity
        self.dimensions = dimensions[1:]
        
        validators.check_dimensions(expected_quantity, *self.dimensions)
        validators.validate_polygon(class_name, expected_quantity)
        
        for value in dimensions:
            validators.validate_positive(value)
    
    @abstractmethod
    def compute_area(self) -> float:
        ...
    
    @abstractmethod
    def compute_perimeter(self) -> float:
        ...