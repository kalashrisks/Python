# input any numbers and check it is positive or negative python

print("Simple if...elif...else")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

print("--------------------------------")

# Using nested if 
print("Using nested if ")

num = float(input("Enter a number : "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

print("--------------------------------")


# If...elif...else

print("using if...elif...else")

num = float(input("Enter a number: "))

if num < 0:
    print("The entered number is negative.")
elif num > 0:
    print("The entered number is positive")
elif num == 0:
    print("Number is zero")
else:
    print("The input is not a number")
        
print("--------------------------------")
