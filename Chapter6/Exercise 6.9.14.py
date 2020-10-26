# Write a function called is_even(n) that takes an integer as an
# argument and returns true if the arguemtn is an even number
# and false if it is odd
import sys

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

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
    test(is_even(5) == False)
    test(is_even(6) == True)
    test(is_even(8) == True)
    test(is_even(1) == False)

test_suite()