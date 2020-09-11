# Modify the turtle bar chart program so that the
# bar for any value of 200 or more is filled with red,
# values between [100 and 200) are filled with yellow,
# and bars representing values less than 100 are filled with green.

import turtle

def drawBar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()               # start filling this shape
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                 # stop filling this shape

def fillColor(t,height):
    if height >=200:
        t.fillcolor("red")
    elif height >= 100 and height < 200:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")
    drawBar(t,height)


xs = [48,117,200,240,160,260,220]  # here is the data
maxheight = max(xs)
numbars = len(xs)
border = 10

tess = turtle.Turtle()           # create tess and set some attributes
#tess.color("blue")
#tess.fillcolor("red")
tess.pensize(3)


wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("lightgreen")
wn.setworldcoordinates(0-border,0-border,40*numbars+border,maxheight+border)


for i in xs:
    fillColor(tess,i)

wn.exitonclick()