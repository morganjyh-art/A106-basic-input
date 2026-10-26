#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
input_a = input("Please enter the value for a: ")
input_b = input("Please enter the value for b: ")
input_c = input("Please enter the value for c: ")
print("The solution for x is: " + str((float(input_c) - float(input_b)) / float(input_a))) 