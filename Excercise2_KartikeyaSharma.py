# Name: Kartikeya Sharma
# Session: Afternoon

import math

# Part A

def minutes_to_milliseconds(minutes):

    milliseconds = minutes * 60000
    return milliseconds

# Part B

def average_of_two_exam_scores(exam1, exam2):

    average = ((exam1 + exam2)/2)
    return average

# Part C

def roots_of_a_quadratic_equation(a, b, c):

    delta = (b**2) - (4*a*c)
    positive_root = ((-b) + math.sqrt(delta))/(2*a)
    negative_root = ((-b) - math.sqrt(delta))/(2*a)

    return positive_root, negative_root

# Part D

def kelvin_to_reaumur(kelvin):

    reaumur = (kelvin - 273.15) * 0.8
    return reaumur

def reaumur_to_celsius(reaumur):

    celsius = reaumur * 1.25
    return celsius

# Part E

def marbles_in_a_cube(cube_side, sphere_radius):

    n = 1

    cube_side = n
    sphere_radius = n/4

    volume_of_cube = cube_side**3
    volume_of_sphere = (4/3)(math.pi)(sphere_radius)**3

    amount_fit = volume_of_cube/volume_of_sphere

    return amount_fit

# part F

def output():

    return print("(PS: \\n, \\t, and loops are not allowed)")

