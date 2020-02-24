# Python program to identify largest number from three number

print("Simple if else loop")
a = float(input("Enter first number a: "))
b = float(input("Enter first number b: "))
c = float(input("Enter first number a: "))

if (a >= b) and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c

print("The largest number is", largest)

print("-------------------------------------------------")


# Creating a list and check which one is large
print("Using List")

a = float(input("Enter first number a: "))
b = float(input("Enter first number b: "))
c = float(input("Enter first number a: "))

list1 = [a, b, c]

list1.sort()

print("Largest element is: ", list1[-1])
print("-------------------------------------------------")

#Using max() function
print("Using max() function")

a = float(input("Enter first number a: "))
b = float(input("Enter first number b: "))
c = float(input("Enter first number a: "))

list1 = [a, b, c]
print("Largest element is: ", max(list1))
print("-------------------------------------------------")

# Find max list element on inputs provided by user
print("Using for loop")
list1 = []
a = int(input("Enter number of elements in list: "))

for i in range(1, a + 1):
    element = int(input("Enter elements: "))
    list1.append(element)

print("Largest element is: ", max(list1))
print("-------------------------------------------------")

