# ####### START OLD CODE #########
# value = 10
# #print("Positive") if value >= 0 else print("Negative")
# ####### END OLD CODE #########

# get input value from the user
value = int(input("Enter a number: "))

# check if the value is positive and odd, and print "Positive and odd" if true
# otherwise, print "The rest"
print("Positive and odd") if (value % 2) == 1 and value >= 0 else print("The rest")