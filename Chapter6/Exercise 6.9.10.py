# Which of these tests fail? Explain why.
import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


test(3 % 4 == 0) #Fails because the remainder between 3 and 4 is NOT 0
test(3 % 4 == 3) # Works because the remainder can only reach 3
test(3 / 4 == 0) # Fails because 3 divided by 4 is exactly 0.75 and not 0
test(3 // 4 == 0) # Works because the result is 0,something which is ok when using //
test(3+4  *  2 == 14) # Fails because 8 + 3 is not 14
test(4-2+2 == 0) # Fails because 4 + 2 - 2 is not 0
test(len("hello, world!") == 13) # There is 13 letters (space and , aswell) in Hello, world!
