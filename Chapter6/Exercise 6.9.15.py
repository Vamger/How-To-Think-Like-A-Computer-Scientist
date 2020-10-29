# Now write the function is_odd(n) that returns True
# when n is odd and False otherwise.
# Include unit tests for this function too.
#
# Finally, modify it so that it uses a call to is_even
# to determine if its argument is an odd integer,
# and ensure that its test still pass.

import sys




def is_odd(n):
    return n % 2 != 1 and not is_even(n)

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
