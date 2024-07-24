import math
import unittest

from geometry.shapes import Circle, Triangle
from geometry.utils import calculate_area


class TestShapes(unittest.TestCase):
    
    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)
        
    def test_circle_zero_radius(self):
        circle = Circle(radius=0)
        self.assertEqual(circle.area(), 0)
    
    def test_circle_negative_radius(self):
        with self.assertRaises(ValueError):
            Circle(radius=-5)

    def test_triangle_area(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=5)
        self.assertAlmostEqual(triangle.area(), 6, places=5)
    
    def test_triangle_zero_side(self):
        with self.assertRaises(ValueError):
            Triangle(side_a=0, side_b=4, side_c=5) 
    
    def test_triangle_invalid_sides(self):
        with self.assertRaises(ValueError):
            Triangle(side_a=1, side_b=2, side_c=10)
    
    def test_calculate_area_circle(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(calculate_area(circle), 78.53981633974483, places=5)
    
    def test_calculate_area_triangle(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=5)
        self.assertAlmostEqual(calculate_area(triangle), 6, places=5)
    
    def test_right_triangle(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=5)
        self.assertTrue(triangle.is_right_triangle())
    
    def test_not_right_triangle(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=6)
        self.assertFalse(triangle.is_right_triangle())
    
    def test_triangle_right_triangle_check_with_large_numbers(self):
        triangle = Triangle(side_a=3000, side_b=4000, side_c=5000)
        self.assertTrue(triangle.is_right_triangle())

    def test_circle_small_radius(self):
        circle = Circle(radius=0.1)
        self.assertAlmostEqual(circle.area(), math.pi * 0.1 ** 2, places=5)
    
    def test_triangle_large_numbers(self):
        triangle = Triangle(side_a=10000, side_b=10000, side_c=10000)
        expected_area = (math.sqrt(3) / 4) * (10000 ** 2)
        self.assertAlmostEqual(triangle.area(), expected_area, places=2)

    def test_triangle_invalid_values(self):
        with self.assertRaises(ValueError):
            Triangle(side_a=-1, side_b=4, side_c=5)
        with self.assertRaises(ValueError):
            Triangle(side_a=1, side_b=2, side_c=-3)


if __name__ == "__main__":
    unittest.main()
