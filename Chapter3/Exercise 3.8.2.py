# Give three attributes of your cellphone object. Give three methods of your cellphone

import turtle


# --------------------------------------------------- "
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("My Phones")

# Give three attributes of your cellphone object
iphone = turtle.Turtle()
samsung = turtle.Turtle()
xperia = turtle.Turtle()

# ----------------------------------------------     "
# Give three methods of your cellphones
samsung.color("blue")
iphone.color("yellow")
xperia.color("green")

samsung.forward(100)
samsung.left(100)
samsung.forward(200)
samsung.right(180)

iphone.forward(200)
iphone.right(100)

xperia.backward(200)
xperia.right(200)


wn.mainloop()

# ------------------------------------------------------- #
# Dumps
# location = ['6', '4', '+']
# operator = ["6", "7"]
# main_number = ("2", "3", "2", "8", "5", "0", "4")

# location.sort(reverse=False)
# operator.sort(reverse=False)
# main_number.__str__()

# print(location, operator, main_number)




