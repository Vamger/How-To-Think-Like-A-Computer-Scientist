# 12. Many interesting shapes can be drawn by the turtle by giving a list of pairs like we did above,
# where the first item of the pair is the angle to turn, and the second item is the distance to move forward.
# Set up a list of pairs so that the turtle draws a house with a cross through the centre, as show here.
# This should be done without going over any of the lines / edges more than once, and without lifting your pen.

import turtle

wn = turtle.Screen()
house = turtle.Turtle()
house.pensize(5)

data = [(135, 200), (225, 150), (135, 110), (90, 110),
        (45, 145), (135, 210),(225, 145), (270, 150)]

def draw_house():
    for (x, y) in data:
        house.left(x)
        house.forward(y)


draw_house()
wn.mainloop()





'''
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

'''