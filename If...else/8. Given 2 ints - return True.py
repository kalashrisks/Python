"""
Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
makes10(9, 10) -> True
makes10(9,9) -> False
makes10(1,9) -> True
"""
# Method 1:
def makes10(a,b):
    sum = a + b
    if(a == 10 or b == 10 or sum == 10):
        return True
    else:
        return False

print(makes10(9, 10))
print(makes10(9, 9))
print(makes10(1, 9))

print("_____________________________________")

###############################################################
# Method 2

a = float(input("Enter a number: "))
b = float(input("Enter b number: "))

def makes10(a,b):
    sum = a + b
    if(a == 10 or b == 10 or sum == 10):
        return True
    else:
        return False

print(makes10(a,b))

print("_____________________________________")

###################################################################

# Method 3
a = float(input("Enter a number: "))
b = float(input("Enter b number: "))

def makes10(a,b):
    if a == 10 or b == 10 or a+b == 10:
        return True
    else:
       return False

print(makes10(a,b))
