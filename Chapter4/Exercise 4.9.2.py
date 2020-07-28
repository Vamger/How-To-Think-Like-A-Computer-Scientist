# Write a program to draw this, Assume the innermost square is 20 units per side
# and each successive square is 20 units bigger, per side, then the one inside
import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()
Window.bgcolor("lightgreen")
Tom.pencolor("hotpink")
Tom.pensize(3)



def DrawASquare(sidelength, CentXcor, CentYcor):
    Tom.penup()
    Tom.goto(CentXcor, CentYcor)
    Tom.goto(Tom.xcor() - sidelength / 2, Tom.ycor())
    Tom.pendown()
    Tom.goto(Tom.xcor(), Tom.ycor() + sidelength / 2)
    Tom.goto(Tom.xcor() + sidelength, Tom.ycor())
    Tom.goto(Tom.xcor(), Tom.ycor() - sidelength)
    Tom.goto(Tom.xcor() - sidelength, Tom.ycor())
    Tom.goto(Tom.xcor(), Tom.ycor() + sidelength / 2)
    Tom.penup()
    Tom.goto(CentXcor, CentYcor)


for i in range(20, 120, 20):
    DrawASquare(i, 0, 0)
Window.mainloop()