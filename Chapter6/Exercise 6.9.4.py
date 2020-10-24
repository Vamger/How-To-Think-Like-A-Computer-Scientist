# Write a function that helps answer questions like ‘“Today is Wednesday.
# I leave on holiday in 19 days time. What day will that be?”’
# So the function must take a day name and a delta argument —
# the number of days to add — and should return the resulting day name:

'''
test(day_add("Monday", 4) ==  "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")
'''


def