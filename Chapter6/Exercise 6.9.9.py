# Write three functions that are the “inverses” of to_secs:




'''
---------------------------------------------------------------------------------------------------


# 1.    hours_in returns the whole integer number of hours
#      represented by a total number of seconds.

import sys


def hours_in(x, y, z):
    """x = seconds, y = minutes & z = hours"""
    s = (z + ((y*60)+(x*3600)))
    q = (s//3600)
    return int(q)



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
    test(hours_in(2.5, 0, 10.71) == (9010//3600))
    test(hours_in(2.433, 0, 0) == (8758//3600))

test_suite()


----------------------------------------------------------------------------------------------------


'''

# 2.    minutes_in returns the whole integer number of left over
#      minutes in a total number of seconds,
#      once the hours have been taken out.


def minutes_in():








# 3.    seconds_in returns the left over seconds represented
#      by a total number of seconds.
