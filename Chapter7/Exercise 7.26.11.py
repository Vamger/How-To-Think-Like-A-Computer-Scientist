# 11. Revisit the drunk pirate problem from the exercises in chapter 3.
# This time, the drunk pirate makes a turn, and then takes some steps forward, and repeats this.
# Our social science student now records pairs of data: the angle of each turn,
# and the number of steps taken after the turn.
#
# Her experimental data is [(160, 20), (-43, 10), (270, 8), (-43, 12)].
# Use a turtle to draw the path taken by our drunk friend.


import turtle
wn = turtle.Screen()
pirate = turtle.Turtle()
pirate.pensize(1)

path = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

def drunken_pirate():
    for (x, y) in path:
        pirate.left(x)
        pirate.forward(y)


drunken_pirate()
wn.mainloop()

