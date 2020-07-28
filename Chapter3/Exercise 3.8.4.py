# Suppose out turtle tess is at heading 0 - facing east.
# We execute the statement tess.left(3645).
# What does tess do, and what is her final heading?

# Answer
# The code will not execute because 3645 is an invalid degree value , however since we
# gave the value 0 on the module tess it means she would move 0 units. Tess will stand still

# However if we 3645//360 --> that gives a rest of 45.
# This means that she would move with a angle of 45 %, which would move her northeast

# Example

import turtle
wn = turtle.Screen()
wn.bgcolor("white")
tess = turtle.Turtle()
tess.shape("circle")
tess.color("red")

tess.left(45)
tess.forward(100)

wn.mainloop()
