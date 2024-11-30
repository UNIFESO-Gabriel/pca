import math
import unittest
from geometry_lib.shapes.base import Polygon
from geometry_lib import ShapeFactory, ShapeType


class TestGeometryLibrary(unittest.TestCase):
    def test_circle_calculations(self):
        raio = 5
        circulo: Polygon = ShapeFactory.create(ShapeType.CIRCLE, raio)
        
        area_esperada: float = math.pi * raio ** 2
        perimetro_esperado: float = 2 * math.pi * raio
        
        self.assertAlmostEqual(circulo.compute_area(), area_esperada)
        self.assertAlmostEqual(circulo.compute_perimeter(), perimetro_esperado)
    
    def test_rectangle_calculations(self):
        largura, altura = 4, 6
        retangulo: Polygon = ShapeFactory.create(ShapeType.RECTANGLE, largura, altura, largura, altura)
        
        area_esperada = largura * altura
        perimetro_esperado = 2 * (largura + altura)
        
        self.assertEqual(retangulo.compute_area(), area_esperada)
        self.assertEqual(retangulo.compute_perimeter(), perimetro_esperado)
    
    def test_triangle_calculations(self):
        lados = (3, 4, 5)  # Tripla pitagórica
        triangulo: Polygon = ShapeFactory.create(ShapeType.TRIANGLE, *lados)
        
        # Componentes da fórmula de Heron
        s: float = sum(lados) / 2  # semi-perímetro
        area_esperada: float = math.sqrt(s * (s - lados[0]) * (s - lados[1]) * (s - lados[2]))
        perimetro_esperado: int = sum(lados)
        
        self.assertAlmostEqual(triangulo.compute_area(), area_esperada)
        self.assertEqual(triangulo.compute_perimeter(), perimetro_esperado)
    
    def test_regular_polygon_calculations(self):
        tamanho_lado = 3
        num_lados = 6
        poligono: Polygon = ShapeFactory.create(ShapeType.POLYGON, *([tamanho_lado] * num_lados))
        
        perimetro_esperado = tamanho_lado * num_lados
        apotema: float = tamanho_lado / (2 * math.tan(math.pi / num_lados))
        area_esperada: float = (perimetro_esperado * apotema) / 2
        
        self.assertAlmostEqual(poligono.compute_area(), area_esperada)
        self.assertEqual(poligono.compute_perimeter(), perimetro_esperado)
    
    def test_dimensoes_invalidas(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create(ShapeType.CIRCLE)  # Sem dimensões
        
        with self.assertRaises(ValueError):
            ShapeFactory.create(ShapeType.CIRCLE, -5)  # Dimensão negativa
        
        with self.assertRaises(ValueError):
            ShapeFactory.create(ShapeType.RECTANGLE, 4, 6)  # Dimensões insuficientes
    
    def test_validacao_poligono(self):
        with self.assertRaises(ValueError):
            ShapeFactory.create(ShapeType.POLYGON, 3, 3)  # Menos de 3 lados
        
        with self.assertRaises(ValueError):
            ShapeFactory.create(ShapeType.POLYGON, -3, -3, -3)  # Lados negativos

if __name__ == '__main__':
    unittest.main()