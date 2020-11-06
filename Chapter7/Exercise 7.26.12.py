# 12. Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above,
# where the first item of the pair is the angle to turn, and the second item is the distance to move forward.
# Set up a list of pairs so that the turtle draws a house with a cross through the centre, as show here.
# This should be done without going over any of the lines / edges more than once, and without lifting your pen.

import turtle

wn = turtle.Screen()
house = turtle.Turtle()
house.pensize(5)

def draw_house():

    house.left(135)
    house.forward(200) # Cross 1
    house.left(225)
    house.forward(150)
    house.left(135)
    house.forward(110)
    house.left(90)
    house.forward(110)
    house.left(45)
    house.forward(145)
    house.left(135)
    house.forward(210)
    house.left(225)
    house.forward(145)
    house.left(270)
    house.forward(150)

draw_house()
wn.mainloop()
