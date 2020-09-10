# Write a fruitful function sum_to(n)  that returns the sum of
# all integer numbers up to and including n.
# So sum_to(10) would be 1+2+3..... +10 which would return the value 55


def sum_to(n):
    return (n * (n + 1)/2)

'''' Or we could use this function '''

# def sum_to(n):
    # This will create a list of numbers from 0 to n
    # e.g. range(0, 11) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    list_of_all_integers = range(0, n+1)
    # The sum does exactly what you think it does, adds them all together.
#    return sum(list_of_all_integers)

print(sum_to(10))





