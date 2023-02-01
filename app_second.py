# get input value from the user
value = int(input("Enter a number: "))

# check if the value is positive and odd
if (value % 2) == 1 and value >= 0:
    # if the condition is True, the value is positive and odd
    print("Positive and odd")
else:
    # if the condition is False, the value is either negative, zero, or even
    print("The rest")