# The four compass points can be abbreviated by single-letter
# strings as "N", "E", "S", and "W". Write a function turn_clockwise
# that takes one of these four compass points as its parameters,
# and returns the next compass point in the clockwise direction.
# Hara are some tests that should pass:

test(turn_clockwise("N") == "E")
test(turn_cloclwise("W") == "N")
# You might ask "What is the argument to the function is some other
# value=" For all other cases, the function should return the value None:

test(turn_clockwise(42) == None)
test(turn_clockwise("rubbish") == None )







# def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    dsquared = dx*dx + dy*dy
#    result = dsquared**0,5
#    return result



# distance(4,9,10,15)
