# Write a function find_hypot which, given
# the length of two sides of a right-angled triangle,
# returns the length of the hypotenuse.
# (Hint: x ** 0.5 will return the square root.)


def find_hypot():
    a = input("Define the first side: ")
    b = input("Define the second side: ")

    c = ((int(a) ** 2) + (int(b) ** 2)**0.5)
    print("The side of the hypotenuse is", int(c))

find_hypot()