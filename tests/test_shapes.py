import unittest

from geometry.shapes import Circle, Triangle
from geometry.utils import calculate_area


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(radius=5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=5)

    def test_triangle_area(self):
        triangle = Triangle(side_a=3, side_b=4, side_c=5)
        self.assertAlmostEqual(triangle.area(), 6, places=5)
    
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


if __name__ == "__main__":
    unittest.main()