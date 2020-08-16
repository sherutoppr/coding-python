

print("Welcome to the Right Triangle Solver App ")

# importing library
import math

# Get user input
base = float(input("Enter first leg of right triangle : "))
perpendicular = float(input("Enter second legs of right triangle : "))

# logic
hypotenuse = math.sqrt(base**2 + perpendicular**2)
area = base * perpendicular * 0.500

# rounding of
hypotenuse = round(hypotenuse, 3)
area = round(area, 3)

# summary table
print("hypotenuse is : " + str(hypotenuse))
print("area is : " + str(area))