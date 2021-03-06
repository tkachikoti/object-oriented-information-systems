"""This module contains three classes that represent a Rectangle,
a Circle, and a Point.

The module also contains three functions:
- A function that checks whether a point is in a circle or not.
- A function that checks whether a rectangle is in a circle or not.
- A function that checks whether a rectangle and a circle overlap.

The module also contains a main function that demonstrates the
functionality of the three functions.

There are two imports in this module:
- math is used to calculate the distance between two points.
- copy is used to copy a Point object.

Module by: Tinashe Nigel Kachikoti (@TNKachikoti)
"""
import math
import copy

class Point:
    """Represents a point in 2-D space."""
    def __init__(self, x=0, y=0):
        """Initializes a point with coordinates (x, y).

        :param x: The x-coordinate of the point.
        :type x: int, optional

        :param y: The y-coordinate of the point.
        :type y: int, optional
        """
        self.x = x
        self.y = y

    def __str__(self):
        """Returns a string representation of the point.

        :return: A string representation of the point.
        :rtype: str
        """
        return "({0}, {1})".format(self.x, self.y)

class Circle:
    """A class that represents a circle.
    The circle is defined by its center point and its radius.
    """
    def __init__(self, x=0, y=0, radius=0):
        """Initializes a circle with center point (x, y) and radius.

        :param x: The x-coordinate of the center point.
        :type x: int, optional

        :param y: The y-coordinate of the center point.
        :type y: int, optional

        :param radius: The radius of the circle.
        :type radius: int, optional
        """
        self.center = Point(x, y)
        self.radius = radius
    
    def __str__(self):
        """Returns a string representation of the circle.

        :return: A string representation of the circle.
        :rtype: str
        """
        return "Circle with center {0} and radius {1}".format(
            self.center, self.radius)

class Rectangle:
    """A class that represents a rectangle.
    The rectangle is defined by its width and height.
    """
    def __init__(self, x=0, y=0, width=0, height=0) -> None:
        """Initializes a rectangle with center point (x, y)
        and width and height.

        :param x: The x-coordinate of the center point.
        :type x: int, optional

        :param y: The y-coordinate of the center point.
        :type y: int, optional

        :param width: The width of the rectangle.
        :type width: int, optional

        :param height: The height of the rectangle.
        :type height: int, optional
        """
        self.width = width
        self.height = height
        self.corner = Point(x, y)

    def __str__(self):
        """Returns a string representation of the rectangle.

        :return: A string representation of the rectangle.
        :rtype: str
        """
        return "Rectangle with corner {0}, width {1} and height {2}".format(
            self.corner, self.width, self.height)

def pythagorean_theorem(A, B):
    """Calculates the distance between two points.

    :param A: The length of one side of a triangle.
    :type A: int

    :param B: The length of one side of a triangle.
    :type B: int

    :return: The length of hypotenuse of a triangle.
    :rtype: float"""
    return math.sqrt((A)**2 + (B)**2)

def point_in_circle(point_obj, circle_obj):
    """Checks whether a point is in a circle.

    :param point_obj: The point to be checked.
    :type point_obj: Point

    :param circle_obj: The circle to be checked.
    :type circle_obj: Circle

    :return: True if the point is in the circle, False otherwise.
    :rtype: bool
    """
    x_A = circle_obj.center.x
    x_B = point_obj.x
    y_A = circle_obj.center.y
    y_B = point_obj.y

    hypotenuse = pythagorean_theorem((x_A - x_B), (y_A - y_B))

    if hypotenuse <= circle_obj.radius:
        return True
    else:
        return False

def rect_in_circle(rectangle_obj, circle_obj):
    """Checks whether any corners of a rect fall in/on a circle.

    :param rectangle_obj: The rectangle to be checked.
    :type rectangle_obj: Rectangle

    :param circle_obj: The circle to be checked.
    :type circle_obj: Circle

    :return: True if any corners of the rectangle fall in/on the circle,
    False otherwise.
    :rtype: bool
    """
    hypotenuse = pythagorean_theorem(rectangle_obj.width, rectangle_obj.height)

    if hypotenuse <= (circle_obj.radius * 2):
        return True
    else:
        return False

def rect_circle_overlap(rectangle_obj, circle_obj):
    """Checks whether any corners of a rect fall in/on a circle.

    :param rectangle_obj: The rectangle to be checked.
    :type rectangle_obj: Rectangle

    :param circle_obj: The circle to be checked.
    :type circle_obj: Circle

    :return: True if any corners of the rectangle fall in/on the circle,
    False otherwise.
    :rtype: bool
    """
    p = copy.copy(rectangle_obj.corner)
    if point_in_circle(p, circle_obj):
        return True

    p.x += rectangle_obj.width
    if point_in_circle(p, circle_obj):
        return True

    p.y -= rectangle_obj.height
    if point_in_circle(p, circle_obj):
        return True

    p.x -= rectangle_obj.width
    if point_in_circle(p, circle_obj):
        return True

    return False

def main():
    """Demonstrates the functionality of the three functions."""
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    circle = Circle()
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))

    if __name__ == '__main__':
        main()
