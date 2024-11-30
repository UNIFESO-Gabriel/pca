from typing import Type

from . import primitives
from .base import Polygon, ShapeType


class ShapeFactory:
    
    dict_shapes: dict[ShapeType, Type[Polygon]] = {
        ShapeType.CIRCLE: primitives.Circle,
        ShapeType.RECTANGLE: primitives.Rectangle,
        ShapeType.TRIANGLE: primitives.Triangle,
        ShapeType.POLYGON: primitives.RegularPolygon
    }
    
    @classmethod
    def create(cls, shape_type: ShapeType, *dimensions: float) -> Polygon:
        quantity: int = len(dimensions)
        return cls.dict_shapes[shape_type](quantity, *dimensions)