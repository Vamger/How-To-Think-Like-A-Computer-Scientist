# Write a void function to draw a star, where the lenght of
# each side is 100 units,
# (Hint: You should turn the turtle by 144 degrees at each point.)

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


draw_star(100, 144)


Window.mainloop()