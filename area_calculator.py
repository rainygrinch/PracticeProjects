# calculates the area of a shape which is specified by the user

import math

def area_of_rectangle(length, width):
    area = length * width
    return area

def area_of_circle(radius):
    area = math.pi * (radius**2)
    return area

def area_of_triangle(base, height):
    area = 0.5 * base * height
    return area

# Main program
shape = input("Choose a shape (rectangle, circle, or triangle): ")

if shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    result = area_of_rectangle(length, width)

elif shape == "circle":
    radius = float(input("Enter the radius: "))
    result = area_of_circle(radius)

elif shape == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    result = area_of_triangle(base, height)

else:
    print("Invalid shape choice!")

print(f"The area of the {shape} is: {result}")
