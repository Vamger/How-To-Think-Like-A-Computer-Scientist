# 1. Write a function to count how many odd numbers are in a list.

def count_odd_numbers():
    for i in range(1, 100):
        if i % 2 == 1:
            continue
        print(i)
    print("done")

count_odd_numbers()


