import math

def circle_calc(radius):
    area = math.pi * (radius ** 2)
    circumference = math.pi * (2 * radius)
    diameter = 2 * radius
    return area, circumference, diameter

if __name__=="__main__":
    radius = input("Enter a radius: ")
    radius = float(radius)
    area, circumference, diameter = circle_calc(radius)
    print(f"Area {area}, Circumference {circumference}, Diameter {diameter}")

