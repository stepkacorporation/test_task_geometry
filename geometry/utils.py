from .shapes import Shape


def calculate_area(shape: Shape) -> float:
    """
    Calculate the area of the given shape.

    :param shape: An instance of a shape.
    :return: Area of the shape.
    """

    return shape.area()
