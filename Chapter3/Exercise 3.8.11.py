# Write a progrom to draw a shape like this: (A jewish star)

# import turtle

# wn = turtle.Screen()
# star = turtle.Turtle()
# star.pensize(3)

# star.left(67.5)
# star.forward(100)
# star.right(135)
# star.forward(100)
# star.left(-135)
# star.forward(125)
# star.left(-157.5)
# star.forward(125)
# star.right(135)
# star.forward(100)
# wn.mainloop()


import turtle
wn = turtle.Screen()
star = turtle.Turtle()
star.pensize(3)

#Funny module :)
# star.hideturtle() # make tess invisible

for i in range(5):
    star.left(144)     # to complete the star you need two full rotations which is is 720
    star.forward(100)  # degrees, divided by 5 (the five points to the star) you get 144

# star.showturtle() # make tess visible

wn.mainloop()