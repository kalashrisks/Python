"""
We have a loud talking parrot. The "hour" parameter is the current hour time
in the range 0..23. We are in trouble if the parrot is talking and the hour
is before 7 or after 20. Return True if we are in trouble. 
parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""


# Method 1:

def parrot_trouble(talking,hour):
    if(talking == True) and (hour <= 6 or hour >= 21):
        return True
    else:
        return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
print("-------------------------------------------")

# Method 2:
def parrot_trouble(talking, hour):
    if talking:
        if hour < 7 or hour > 20:
            return True
        else:
            return False
    else:
        return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))

print("-------------------------------------------")

# Method 3:
talking = bool(input("Talking (True/False) =  "))
hours = int(input("Enter number of hours: "))
 
def parrot_trouble(talking, hours):
    if talking == "True":
        if hours < 7 or hours > 20:
            return True
        else:
            return False
    else:
        return False

print(parrot_trouble(talking, hours))
