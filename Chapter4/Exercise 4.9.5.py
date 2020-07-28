# The two spirals in this picture differ only by the turn angle. Draw both.

# ------------------------------------------------------------------- #

'''Picture #1'''

import turtle

'''Create screen & turtle spiral'''
window = turtle.Screen()
window.bgcolor("lightgreen")


spiral = turtle.Turtle()
spiral.pencolor("blue")
spiral.pensize(2)
spiral.speed(10)

waves = turtle.Turtle()
waves.pencolor("blue")
waves.pensize(2)
waves.speed(10)

turtle_object1 = spiral
turtle_object2 = waves

# --------------------------------------------------------------------- #
size = 10

for i in range(100):
    spiral.forward(size)
    spiral.right(90)
    size = size + 2

size = 10

waves.penup()
waves.forward(250)
waves.pendown()

for i in range(100):
    waves.forward(size)
    waves.left(91)
    size = size + 2


# --------------------------------------------------------------------- #

window.mainloop()

