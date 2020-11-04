# 1. Write a function to count how many odd numbers are in a list.

list = [1, 40, 13, 50, 21, 24, 25, 39, 89, 76, 21, 12]

def count_odd_numbers():
    odd_number_count = 0
    for i in list:
        if i % 2 == 1:
            odd_number_count += 1
    print("There are", odd_number_count, "numbers in the list which are odd")


# 2. Sum up all the even numbers in a list.


def sum_even_numbers():
    start_value = 0
    for i in list:
        if i % 2 == 0:
            start_value = start_value + i
    print(start_value)
    print(40+50+24+76+12)

# 3. Sum upp all the negative numbers in a list

list1 = [-3, 10, -45, 90, -430, 100, 12, 43]

def sum_negative_numbers():
    start_value = 0
    for i in list1:
        if i < 0:
            start_value = start_value + i
    print(start_value)

# 4. Count how many words in a list have length 5.

list2 = ["Apple", "Pear", "Computer", "Book", "Cards", "Ball", "Parrot", "Follow", "Balls"]

def count_words():
    w = 0
    for i in list2:
        if len(i) == 5:
            w = w + 1
    print("There are", w, "word(s) in the list which have 5 letters")





# count_odd_numbers()
# sum_even_numbers()
# count_words()


# 5. Sum all the elements in a list up to but not including the first even number.
#    (Write your unit tests. What if there is no even number?)

list3 = [3, 40, 32, 345, 872, 653, 101, 30]

def sum_list_not_first_number():
