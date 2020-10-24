# Can your day_add function already work with negative deltas?
# For example, -1 would be yesterday, or -7 would be a week ago:

import sys

def day_num(x):
    if x == "Monday":
        return 0
    elif x == "Tuesday":
        return 1
    elif x == "Wednesday":
        return 2
    elif x == "Thursday":
        return 3
    elif x == "Friday":
        return 4
    elif x == "Saturday":
        return 5
    elif x == "Sunday":
        return 6
    else:
        return None

def day_name(x):
    if x == int(0):
        return "Monday"
    elif x == int(1):
        return "Tuesday"
    elif x == int(2):
        return "Wednesday"
    elif x == int(3):
        return "Thursday"
    elif x == int(4):
        return "Friday"
    elif x == int(5):
        return "Saturday"
    elif x == int(6):
        return "Sunday"
    else:
        return None

def day_add(y,z):
    day = (day_num(y))
    day2 = ((day + (z%7))%7)
    day3 = ((day_name(day2)))
    return (day3)



def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(day_add("Sunday", -1) == "Saturday")
    test(day_add("Sunday", -7) == "Sunday")
    test(day_add("Tuesday", -100) == "Sunday")


test_suite()