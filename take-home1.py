#CIS 103:  Fundamentals of Programming
#Description: Lab 1: Python Loops and Object Types
#Instructor: Md Ali
#Date: 09/21/2024
#Student: Pierina Brito

#PART 4

#TAKE HOME 1

# 1. Write a program that takes the radius of a sphere (a floating-point number) as input and
# outputs the sphere’s diameter, circumference, surface area, and volume.

import math

# FUNCTION TO CALCULATE AND PRINT THE SPHERE'S PROPERTIES
def sphere_properties(radius):
    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    surface_area = 4 * math.pi * (radius ** 2)
    volume = (4/3) * math.pi * (radius ** 3)

    # PRINT RESULTS
    print(f"Diameter: {diameter:.2f}")
    print(f"Circumference: {circumference:.2f}")
    print(f"Surface Area: {surface_area:.2f}")
    print(f"Volume: {volume:.2f}")

# INPUT FROM USER
radius = float(input("Enter the radius of the sphere: "))

# CALCULATE AND DISPLAY SPHERE PROPERTIES
sphere_properties(radius)








