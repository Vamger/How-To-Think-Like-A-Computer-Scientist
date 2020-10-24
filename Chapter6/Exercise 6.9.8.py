# Extend to_secs so that it can cope with real values as inputs.
# It should always return an integer number of seconds
# (truncated towards zero):

"""
test(to_secs(2.5, 0, 10.71) == 9010)
test(to_secs(2.433,0,0) == 8758)
"""

import sys

def to_secs(x, y, z):
    """z = seconds, y = minutes & x = hours"""
    s = (z + (y*60)+(x*3600))
    return int(s)



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
    test(to_secs(2.5, 0, 10.71) == 9010)
    test(to_secs(2.433, 0, 0) == 8758)

test_suite()