 # Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon.
 # When called with draw_poly(tess, 8, 50), it will draw a shape like this:

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
