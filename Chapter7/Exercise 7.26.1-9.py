# 1. Write a function to count how many odd numbers are in a list.

def count_odd_numbers():
    list = [1, 40, 13, 50, 21, 24, 25, 39, 89, 76, 21, 12]
    odd_number = 0
    for i in list:
        if i % 2 == 1:
            odd_number += 1
    print("There are", odd_number, "numbers in the list which are odd")
    print("done")

count_odd_numbers()


