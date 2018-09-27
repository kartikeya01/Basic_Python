# Name: Kartikeya Sharma
# Session: Afternoon

import math

# Part A

given_minutes = 42
given_seconds = 42

minutes_to_seconds = given_minutes*60

print("Part A:")
print("42 minutes and 42 seconds =", minutes_to_seconds + given_seconds, "seconds\n")

# Part B

radius_1 = 4
radius_2 = 6

volume_of_sphere_1 = (4/3)*math.pi*(radius_1**3)
volume_of_sphere_2 = (4/3)*math.pi*(radius_2**3)

print("Part B:")
print("Volume of a sphere with radius 4 =", volume_of_sphere_1)
print("Volume of a sphere with radius 6 =", volume_of_sphere_2,"\n")

# Part C

value = -40

fahrenheit_to_celsius = (value-32)*(5/9)
celsius_to_fahrenheit = (value*9/5)+32

print("Part C:")
print(value, "Degrees Celsius in Fahrenheit =", celsius_to_fahrenheit, "Degrees")
print(value, "Degrees Fahrenheit in celsius =", fahrenheit_to_celsius, "Degrees\n")

# Part D

a = 1

RP_side_1 = a
RP_side_2 = 2*a
RP_side_3 = 3*a

C_side = a

C_in_RP = (RP_side_1 + RP_side_2 + RP_side_3)/C_side

print("Part D:")
print("Cubes that can fit in the Rectangular Prism = ", C_in_RP)