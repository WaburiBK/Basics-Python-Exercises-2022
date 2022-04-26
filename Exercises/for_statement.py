# Functions in Python

"""
Write a function called calculate_area that takes base and height as
an input and returns the area of a triangle.
"""

base = 10
height = 5

def calculate_area(dimension1, dimension2, shape="triangle"):
    if shape == "triangle":
        area = 1/2 * (dimension1 * dimension2)

    return area

triangle_area = calculate_area(base, height, "triangle")

print("Area of triangle is: ", triangle_area)

