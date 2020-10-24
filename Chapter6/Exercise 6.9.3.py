# Write the inverse function day_num which is
# given a day name, and returns its number:
'''
test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")
'''

# Once again, if this function is given an invalid argument, it should return None:
'''
test(day_num("Halloween") == None)
'''


'''
Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3 = 3
Thursday = 4
Friday = 5
Saturday = 6


'''
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


def day_num(x):
    if x == "Sunday":
        return 0
    elif x == "Monday":
        return 1
    elif x == "Tuesday":
        return 2
    elif x == "Wednesday":
        return 3
    elif x == "Thursday":
        return 4
    elif x == "Friday":
        return 5
    elif x == "Saturday":
        return 6
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
    test(day_num("Friday") == 5)
    test(day_num("Sunday") == 0)
    test(day_num(day_name(3)) == 3)
    test(day_name(day_num("Thursday")) == "Thursday")



test_suite()