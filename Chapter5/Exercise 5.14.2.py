# You go on a wonderful holiday (perhaps to jail,
# # if you don’t like happy exercises) leaving on day number 3 (a Wednesday).
# # You return home after 137 sleeps. Write a general version of the program
# which asks for the starting day number, and the length of your stay,
# and it will tell you the name of day of the week you will return on.
from typing import List, Any

def define_day():
    lst = list(range(200))
    day = input("Which day are you going to leave, if day 0 is monday and day 7 is sunday? ")
    if int(day) in lst[1:200:7]:
        print("The day is Monday")
    elif int(day) in lst[2:200:7]:
        print("The day is Tuesday")
    elif int(day) in lst[3:200:7]:
        print("The day is Wednesday")
    elif int(day) in lst[4:200:7]:
        print("The day is Thursday")
    elif int(day) in lst[5:200:7]:
        print("The day is Friday")
    elif int(day) in lst[6:200:7]:
        print("The day is Saturday")
    elif int(day) in lst[7:200:7]:
        print("The day is Sunday")
    else:
        print("Invalid value!")


define_day()
