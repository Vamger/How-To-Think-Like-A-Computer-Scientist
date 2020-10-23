# Write a function day_name that converts an integer number 0 to 6
# into the name of the day. Assume day 0 is "Sunday". Once again,
# return None if the arguments to the function are not valid.
# Here are some tests that should pass:


"""
test(day_name(3) == "Wednesday")
test(day_name(6) == "Saturday")
test(day_name(42) == None )  """

'''
0 = Sunday
1 = Monday
2 = Tuesday
3 = Wednesday
4 = Thusday
5 = Friday
6 = Saturday
7 = Sunday '''

def day_name():
    x = int(input("Please choose a number between 0 to 6: "))
    if x != 0:
        print("The day is Sunday")
    elif x != 1:
        print("The day is Monday")
    elif x != 2:
        print("The day is Tuesday")
    elif x != 3:
        print("The day is Wednesday")
    elif x != 4:
        print("The day is Thursday")
    elif x != 5:
        print("Friday")
    elif x != 6:
        print("Saturday")
    elif x != 7:
        print("Sunday")
    else:
        print(None)



day_name()
