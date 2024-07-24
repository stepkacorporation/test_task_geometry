import math

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Method to calculate the area of the shape. Must be implemented in derived classes."""
        
        raise NotImplementedError
    

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        """
        Initialize a circle.

        :param radius: Radius of the circle.
        """

        self.radius = radius
    
    def area(self) -> float:
        """
        Calculate the area of the circle.

        :return: Area of the circle.
        """

        return math.pi * self.radius ** 2
    

class Triangle(Shape):
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        """
        Initialize a triangle.

        :param side_a: Length of the first side.
        :param side_b: Length of the second side.
        :param side_c: Length of the third side.
        """

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self) -> float:
        """
        Calculate the area of the triangle using Heron's formula.

        :return: Area of the triangle.
        """

        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def is_right_triangle(self) -> bool:
        """
        Check if the triangle is a right triangle.

        :return: True if the triangle is a right triangle, else False.
        """

        sides = sorted([self.side_a, self.side_b, self.side_c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
    