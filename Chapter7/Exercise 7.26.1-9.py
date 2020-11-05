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






# 5. Sum all the elements in a list up to but not including the first even number.
#    (Write your unit tests. What if there is no even number?)

list3 = [3, 40, 1, 5, 2, 3, 10]

def sum_list_not_first_number():
    start_value = 0
    once = False
    for i in list3:
        if i % 2 == 0 and not once:
            once = True
            continue
        start_value = start_value + i
    print(start_value)


# 6. Count how many words occur in a list up to and including
# the first occurrence of the word “sam”.
# (Write your unit tests for this case too. What if “sam” does not occur?)

list4 = ["adam", "frodo", "samuel", "gandalf", "sam",
         "aragorn", "legolas", "gimli", "monster"]

def count_words_w_sam():
    start_value = 0
    for i in list4:
        if i == "sam":
            break
        start_value = start_value + 1
    print("There are", start_value + 1, "words in the list once reaching and including the word sam")


# count_odd_numbers()
# sum_even_numbers()
# sum_negative_numbers()
# count_words()
# sum_list_not_first_number()
# count_words_w_sam()

# 7. Add a print function to Newton’s sqrt function that prints out better each time it is calculated.
# Call your modified function with 25 as an argument and record the results.


# Newtons sqare root function --> f(x) = ( x + 4/x)/2 = y
# Make a continous statement, i.e. f(x) = ( y + 4/y)/2 = z
#                                    f(x) = (z + 4/z)/2 = q
# etc

def newton_sqrt(a):
    f1 = (a + (4/a))/2
    while f1 <= 25:
        f2 = (f1 + (4/f1))/2
        print(f2)
        if abs(f1-f2) < 0.0001:
            return f2
        f1 = f2

newton_sqrt(25)

'''

def sqrt(a):
    """Modify function square root. Printing out "better" result when
    processing each time in loop"""
    approx = a/2.0
    while True:
        better = (approx + a/approx)/2.0
        print (better)
        if abs(approx - better) < 0.0001:
            return better
        approx = better

sqrt(25)

'''