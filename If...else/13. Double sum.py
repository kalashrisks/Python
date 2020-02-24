"""
Given two int values, return their sum. Unless the two values are the same, 
then return double their sum. 
sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""
# Method 1
def sum_double(a,b):
    if a!= b:
        return a + b
    else:
        return 2 * ( a + b)

print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))

print("--------------------------------")

# Method 2
def sum_double(a,b):
    result = a + b
    if(a == b):
        result = 2 * result
    return result
print(sum_double(1, 2))
print(sum_double(3, 2))
print(sum_double(2, 2))

print("--------------------------------")

# Method 3
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
def sum_double(a,b):
    result = a + b
    if (a==b):
        result = 2*result
    return result

print(sum_double(a,b))

print("--------------------------------")

# Method 4
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
def sum_double(a,b):
    sum = a + b
    return sum if a != b else 2 * sum
print(sum_double(a,b))

