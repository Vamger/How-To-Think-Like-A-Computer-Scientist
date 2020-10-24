# Write a function that helps answer questions like ‘“Today is Wednesday.
# I leave on holiday in 19 days time. What day will that be?”’
# So the function must take a day name and a delta argument —
# the number of days to add — and should return the resulting day name:

'''
test(day_add("Monday", 4) ==  "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")
'''

import sys

'''

Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6

Monday = 
'''

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
    test(day_add("Monday", 4) == "Friday")
    test(day_add("Tuesday", 0) == "Tuesday")
    test(day_add("Tuesday", 14) == "Tuesday")
    test(day_add("Sunday", 100) == "Tuesday")


test_suite()