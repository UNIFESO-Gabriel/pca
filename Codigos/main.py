from geometry_lib import ShapeFactory, ShapeType
from geometry_lib.shapes.base import Polygon

if __name__ == "__main__":

    # Criar e usar formas
    circle: Polygon = ShapeFactory.create(ShapeType.CIRCLE, 5)
    print(f"Circle area: {circle.compute_area():.2f}")
    print(f"Circle circunference: {circle.compute_perimeter():.2f}")

    rectangle: Polygon = ShapeFactory.create(ShapeType.RECTANGLE, 4, 6, 4, 6)
    print(f"Rectangle area: {rectangle.compute_area():.2f}")
    print(f"Rectangle perimeter: {rectangle.compute_perimeter():.2f}")

    # Criando triângulo para cálculo de área
    triangle: Polygon = ShapeFactory.create(ShapeType.TRIANGLE, 3, 4, 5)
    print(f"Triangle area: {triangle.compute_area():.2f}")
    print(f"Triangle perimeter: {triangle.compute_perimeter():.2f}")
    
    # Criando polígono para cálculo de área
    polygon: Polygon = ShapeFactory.create(ShapeType.POLYGON, *((3,) * 6))
    print(f"Polygon area: {polygon.compute_area():.2f}")
    print(f"Polygon perimeter: {polygon.compute_perimeter():.2f}")