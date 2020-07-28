# Draw this pretty pattern

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Pretty pattern")


tess = turtle.Turtle()
alex = turtle.Turtle()
mike = turtle.Turtle()

turtle_objects = tess, alex, mike

for t in turtle_objects:
    t.pencolor("blue")
    t.pensize(3)
    t.speed(10)


def draw_circle(turtle_objects, n):
    turtle_objects.penup()
    turtle_objects.goto(6, 0)
    turtle_objects.pendown()
    for i in range(n):
        turtle_objects.forward(50)
        turtle_objects.left(360/n)
    return turtle_objects


def draw_spiderweb(turtle_objects, m):
    turtle_objects.penup()
    turtle_objects.goto(30, 150)
    turtle_objects.pendown()
    for i in range(m):
        turtle_objects.forward(150)
        turtle_objects.penup()
        turtle_objects.forward(-150)
        turtle_objects.pendown()
        turtle_objects.left(360/m)
    return turtle_objects


def draw_square(turtle_objects, n):
        turtle_objects.penup()
        turtle_objects.goto(30, 150)
        turtle_objects.pendown()
        for i in range(n):
            for j in range(n):
                turtle_objects.forward(150)
                turtle_objects.left(90)
            return turtle_objects


def draw_squares(turtle_objects, p, m):
    for i in range(p):
        turtle_objects.left(360/m)
      #  if i == int(4):
      #      print(4) # continue
        turtle_objects.penup()
        draw_square(mike, 4)
    return turtle_objects


draw_circle(tess, 19)
draw_spiderweb(alex, 19)
draw_square(mike, 4)
draw_squares(mike, 19, 19)


window.mainloop()

