# Use for loops to make a turtle draw these regular polygons
# (regular means all sides the same lengths, all angles the same):

# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)

import turtle

wn = turtle.Screen()
wn.bgcolor('white')

'''Triangle three sides 360//3 = 120'''
ted = turtle.Turtle()
ted.color('green')
ted.forward(100)
ted.left(120)
ted.forward(100)
ted.left(120)
ted.forward(100)


'''Square four sides 360//4 = 90'''
alex = turtle.Turtle()
alex.color('blue')
alex.forward(300)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)
alex.left(90)
alex.forward(100)


'''Hexagon Six sides 360//6 = 60'''

tess = turtle.Turtle()
tess.color('yellow')
for i in range(6):
    tess.pensize(4)
    tess.backward(100)
    tess.right(60)


'''Octagon eight sides 460/8 = 45'''
taz = turtle.Turtle()
taz.color('pink')
for i in range (8):
    taz.pensize(10)
    taz.backward(200)
    taz.right(45)

wn.mainloop()

