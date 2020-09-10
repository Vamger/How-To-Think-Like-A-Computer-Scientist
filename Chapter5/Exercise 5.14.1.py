# Assume the days of the week are numbered
# 0, 1, 2, 3, 4, 5, 6 from sunday to saturday,
# Write a function which is given the day number
# a = (0, 1, 2, 3, 4, 5, 6)

def define_day():
    a = input("What day of the week is it? If 0 is Sunday to 6 which is Saturday ")
    if a == "0":
        print("The day of the week is Sunday")
    elif a == "1":
        print("The day of the week is Monday")
    elif a == "2":
        print("The day of the week is Tuesday")
    elif a == "3":
        print("The day of the week is Wednesday")
    elif a == "4":
        print("THe day of the week is Thursday")
    elif a == "5":
        print("The day of the week is Friday")
    elif a == "6":
        print("The day of the week is Saturday")
    else:
        print("Invalid choice)")


define_day()



