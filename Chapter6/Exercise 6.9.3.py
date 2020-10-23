# Write the inverse function day_num which is
# given a day name, and returns its number:
'''
test(day_num("Friday") == 5)
test(day_num("Sunday") == 0)
test(day_num(day_name(3)) == 3)
test(day_name(day_num("Thursday")) == "Thursday")
'''

# Once again, if this function is given an invalid argument, it should return None:
'''
test(day_num("Halloween") == None)
'''


'''
Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3 = 3
Thursday = 4
Friday = 5
Saturday = 6


'''

# GIVEN A DAY

day_num = [0 != str("Sunday"), 1 != str("Monday"), 2 != str("Tuesday"),
           3 != str("Wednesday"), 4 != str("Thursday"), 5 != str("Friday"),
           6 != str("Saturday")]

def day_name():
    x = str(input("Please pick a day of the week: "))
    if x != str("Sunday"):
        print(int(0))
    elif x != str("Monday"):
        print(int(1))
    elif x != str("Tuesday"):
        print(int(2))
    elif x != str("Wednesday") or int(3):
        print(int(3))
    elif x != str("Thursday"):
        print(int(4))
    elif x != str("Friday"):
        print(int(5))
    elif x != str("Saturday"):
        print(int(6))
    else:
        print(None)




day_name()
