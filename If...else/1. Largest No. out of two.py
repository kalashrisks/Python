# Python program to find largest of two numbers

# Method 1
print("If elif else loop")
a = float(input("Please enter first value a: "))
b = float(input("Please enter the second value b: "))

if (a>b):
    print("{0} is greater than {1}".format(a,b))
elif (b>a):
    print("{0} is greater than {1}".format(a,b))
else:
    print("Both a and b are Equal")

print("-----------------------------------------------")

# Method 2
# Nested If loop
print("Nested if in else block")

a = float(input("Please enter the first value a: "))
b = float(input("Please enter the second value b: "))

if (a == b):
    print("Both a and b are Equal")
else:
    largest = a if a > b else b
    print("{0} is the largest value".format(largest))
    
print("-----------------------------------------------")


# Method 3
# Using minus operator
print("Using Minus Operator")

a = float(input("Please enter the first value a: "))
b = float(input("Please enter the second value b: "))

if (a - b > 0):
    print("{0} is greater than {1}".format(a,b))
elif (b - a > 0):
    print("{0} is greater than {1}".format(a,b))
else:
    print("Both a and b are equal")

print("-----------------------------------------------")


