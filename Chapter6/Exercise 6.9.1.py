import sys

# The four compass points can be abbreviated by single-letters
# strings as "N", "E", "S", and "W". Write a function turn_clockwise
# that takes one of these four compass points as its parameters,
# and returns the next compass point in the clockwise direction.
# Hara are some tests that should pass:





''' test(turn_clockwise("N") == "E")
test(turn_cloclwise("W") == "N") '''

# You might ask "What is the argument to the function is some other
# value=" For all other cases, the function should return the value None:

'''
test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None ) '''

# https://planetcalc.com/7041/

# A Compass has directions from 1 -> 32

# N = 1 to 8
# E = 9 - 16
# S = 17 - 24
# W = 25 - 32

def turn_clockwise(x):
    if x == "N":
        return "E"
    elif x == "E":
        return "S"
    elif x == "S":
        return "W"
    elif x == "W":
        return "N"
    else:
        return None

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    test(turn_clockwise(42) == None)
    test(turn_clockwise("rubbish") == None)
    test(turn_clockwise("N") == "E")
    test(turn_clockwise("W") == "N")

test_suite()



# def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    dsquared = dx*dx + dy*dy
#    result = dsquared**0,5
#    return result



# distance(4,9,10,15)
