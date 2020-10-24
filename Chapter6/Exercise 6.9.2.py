# Write a function day_name that converts an integer number 0 to 6
# into the name of the day. Assume day 0 is "Sunday". Once again,
# return None if the arguments to the function are not valid.
# Here are some tests that should pass:


"""
test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None )  """

'''
0 = Sunday
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thusday
5 = Friday
6 = Saturday
7 = Sunday '''

import sys

def day_name(x):
    if x == int(0):
        return "Sunday"
    elif x == int(1):
        return "Monday"
    elif x == int(2):
        return "Tuesday"
    elif x == int(3):
        return "Wednesday"
    elif x == int(4):
        return "Thursday"
    elif x == int(5):
        return "Friday"
    elif x == int(6):
        return "Saturday"
    elif x == int(7):
        return "Sunday"
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
    test(day_name(3) == "Wednesday")
    test(day_name(6) == "Saturday")
    test(day_name(42) == None)



test_suite()