# Write three functions that are the “inverses” of to_secs:

'''
1.    hours_in returns the whole integer number of hours
    represented by a total number of seconds.


2.    minutes_in returns the whole integer number of left over
      minutes in a total number of seconds,
      once the hours have been taken out.


3.    seconds_in returns the left over seconds represented
      by a total number of seconds.

You may assume that the total number of seconds passed to these functions is an integer. Here are some test cases:

test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)




'''

import sys


def hours_in(x):
    """x = seconds"""
    p = (x//3600)
    return int(p)


def minutes_in(x):
    """x = seconds"""
    q = ((x%3600)//60)
    return int(q)

def seconds_in(x):
    a = ((x%3600))
    b = (a%60)
    return int(b)

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
    test(hours_in(9010) == 2)
    test(minutes_in(9010) == 30)
    test(seconds_in(9010) == 10)

test_suite()




