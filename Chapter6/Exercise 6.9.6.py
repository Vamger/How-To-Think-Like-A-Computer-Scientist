# Write a function days_in_month which takes the name
# of a month, and returns the number of days in the month.
# Ignore leap years:

'''
test(days_in_month("February") == 28)
test(days_in_month("December") == 31)
'''
import sys

'''
Januari = 31
Februari = 28
March = 31
April = 30
May = 31
June = 30
July = 31
August = 31
September = 30
October = 31
November = 30
December = 31
'''


def days_in_month(x):
    if x == "January":
        return int(31)
    elif x == "February":
        return int(28)
    elif x == "March":
        return int(31)
    elif x == "April":
        return int(30)
    elif x == "May":
        return int(31)
    elif x == "June":
        return int(30)
    elif x == "July":
        return int(31)
    elif x == "August":
        return int(31)
    elif x == "September":
        return int(30)
    elif x == "October":
        return int(31)
    elif x == "November":
        return int(30)
    elif x == "December":
        return int(31)
    else:
        return None




def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(days_in_month("February") == 28)
    test(days_in_month("December") == 31)

test_suite()