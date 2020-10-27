# Now write the function is_odd(n) that returns True
# when n is odd and False otherwise.
# Include unit tests for this function too.
#
# Finally, modify it so that it uses a call to is_even
# to determine if its argument is an odd integer,
# and ensure that its test still pass.

import sys

def is_odd(n, x):
    if n % 2 != 0:
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
    test(is_odd(5) == False)
    test(is_odd(6) == True)
    test(is_odd(8) == True)
    test(is_odd(1) == False)

test_suite()