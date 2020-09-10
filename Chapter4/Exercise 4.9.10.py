# Extend your program above. Draw five stars, but between each,
# pick up the pen, move forward by 350 units,
# turn right by 144, put the pen down, and draw the next star

import turtle

Window = turtle.Screen()
star = turtle.Turtle()
Window.bgcolor("lightgreen")
star.pencolor("hotpink")
star.pensize(3)


def draw_star(s, t):
    for i in range(5):
        star.forward(s)
        star.left(t)
        continue
    star.penup()
    star.forward(350)
    star.right(144)
    star.pendown()


draw_star(100, 144)
draw_star(100, 144)
draw_star(100, 144)
draw_star(100, 144)
draw_star(100, 144)

Window.mainloop()