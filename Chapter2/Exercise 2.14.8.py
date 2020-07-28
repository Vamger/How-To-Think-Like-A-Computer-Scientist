print("Hi!\n")

time_now = int(input("What is the current time?: "))
time_passed = int(input("Enter the amount of time that will pass for the alarm to go off: "))


time_alarm = (time_now + time_passed) % 24

print("The alarm will go off at", str(time_alarm), "if", time_passed, "hours has passed")


