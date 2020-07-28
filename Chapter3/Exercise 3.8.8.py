# Enhance your program above to also tell us what the drunk pirate's heading is
# after he has finished stumbling around. (Assume he begins at heading 0)

import turtle
import random

wn = turtle.Screen()
wn.bgcolor('white')


pirate = turtle.Turtle()

for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    pirate.left(i)
    print("The pirate is heading", str(i), "degres to the left")
    pirate.forward(100)
    print("The pirate is moving 100 units")


wn.mainloop()
