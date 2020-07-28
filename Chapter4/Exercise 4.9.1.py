# Write a void (non-fruitful) function to draw a square.
# Use it in a program to draw the image shown below.
# Assume each side is 20 units.
# (Hint: notice that the turtle has already moved away from the
# ending point of the last square when the program ends.)

import turtle


def create_window(color, title):
    """Creates a turtle window and return it"""
    window = turtle.Screen()
    window.bgcolor(color)
    window.title(title)
    return window


def create_turtle(color, pensize):
    """Create a turtle object and returns it"""
    turtle_object = turtle.Turtle()
    turtle_object.color(color)
    turtle_object.pensize(pensize)
    return turtle_object


def draw_square(turtle_object, number, length_of_size):
    """Draws 'number' squares/s in the screen"""
    for i in range(number):
        for j in range(4):      #draw square
            turtle_object.forward(length_of_size)
            turtle_object.left(90)

        turtle_object.penup()       # put a space for the next square
        turtle_object.forward(40)
        turtle_object.pendown()


window = create_window("lightgreen", "squares")
pointer = create_turtle("hotpink", 3)

pointer.penup()
pointer.forward(-100)
pointer.pendown()

draw_square(pointer, 5, 20)

window.mainloop()


# def assign_tess():
#   tess.pensize(3)
#    tess.color("hotpink")


#def draw_a_square(t, sz):
#    t.pendown()
#    t.forward(sz)
#    t.left(90)
#    t.penup()


# def draw_squares():
#    for i in range(4):
#        draw_a_square(tess, 20)
#        tess.forward(20)
#        # t.forward(40)


# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()

# assign_tess()
# draw_a_square(tess, 40)
# draw_squares()

# wn.mainloop()

