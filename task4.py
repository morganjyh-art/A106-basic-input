#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
input_radius = input("Please enter the radius: ")
input_height = input("Please enter the height: ")  
print("The surface area of the cone is: " + str(math.pi * float(input_radius) * (float(input_radius) + math.sqrt(float(input_height)**2 + float(input_radius)**2))))