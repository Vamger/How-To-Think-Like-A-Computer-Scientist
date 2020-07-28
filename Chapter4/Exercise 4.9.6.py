# Write a void function draw_equitriangle(t, sz) which calls
# draw_poly form the previous question to have its turtle draw a equilateral (liksidig) triangle

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)


def draw_poly(t, n, sz):
    tess.goto(50, 0)
    for i in range(n-1):
        t.right(-45)
        t.forward(sz)
    t.left(45)

draw_poly(tess, 8, 50)

window.mainloop()



alex = turtle.Turtle()

def draw_equitriangle(t, sz):
    draw_poly