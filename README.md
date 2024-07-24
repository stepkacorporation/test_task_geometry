# Geometry Library (Test Task)

This library provides classes and functions to calculate the area of various geometric shapes, including circles and triangles.

## Installation

You can install the library directly from the GitHub repository:
```bash
pip install git+https://github.com/stepkacorporation/test_task_geometry.git
```

Alternatively, you can clone the repository and install it locally:
```bash
git clone https://github.com/stepkacorporation/test_task_geometry.git
cd test_task_geometry
pip install .
```

## Usage

```python
from geometry.shapes import Circle, Triangle
from geometry.utils import calculate_area

# Create a circle with radius 5 and calculate its area
circle = Circle(radius=5)
print("Circle area:", calculate_area(circle))

# Create a triangle with sides 3, 4, and 5 and calculate its area
triangle = Triangle(side_a=3, side_b=4, side_c=5)
print("Triangle area:", calculate_area(triangle))
print("Is the triangle a right triangle:", triangle.is_right_triangle())
```
Output:
```
Circle area: 78.53981633974483
Triangle area: 6.0
Is the triangle a right triangle: True
```

## Running Tests

To run the tests, you can use the unittest module:
```bash
python -m unittest discover -s tests
```
