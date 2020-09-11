# In the turtle bar chart program, what do you
# expect to happen if one or more of the data
# values in the list is negative? Try it out.
# Change the program so that when it prints the
# text value for the negative bars,
# it puts the text below the bottom of the bar.

import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height)
    if height > 0:
        t.write("  " + str(height))
    else:
        t.write("  " + str(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.forward(10)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [48,-117,-200,240,-160,-260,220]

for a in xs:
    draw_bar(tess, a)

wn.mainloop()