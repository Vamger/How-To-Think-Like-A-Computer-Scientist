# Write a function area_of_circle(r) which returns
# the area of a circle of radius r
import math


def area_of_circle(r):
    a = math.pi * (r**2)
    return a


print(area_of_circle(2))