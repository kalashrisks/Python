# Input positive number and check it is even or odd

print("If...elif...else")
num = float(input("Enter a number: "))
# Check if it is positive or negative
if num > 0:
    print("Positive number")
elif num == 0:
    print("zero")
else:
    print("Negative number")

# Checking for odd and even
if (num % 2) == 0:
    print("{0} is even".format(num))
else:
    print("{0} is Odd".format(num))

print("---------------------------------")

# Nested if

print("Nested if")
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# Checking for odd and even
if (num % 2)== 0:
          print("{0} is Even".format(num))
else:
    print("{0} is odd".format(num))
