"""
Given a string, return a new string where "not " has been added to the front.
However, if the string already begins with "not", return the string unchanged.
not_string('school') → 'not school'
not_string('parrot') → 'not parrot'
not_string('not working') → 'not working'
"""

# Method 1
def not_string(str):
    for i in range(0, len(str)):
        if str[0:3] == 'not':
            return str
        else:
            return "not " + str

print(not_string('school'))
print(not_string('parrot'))
print(not_string('not working'))

print("________________________________________")

# Method 2

def not_string(str):
    a = str.split("not")
    if len(a) > 1 and a[0]=="":
        return str
    else:
        return "not " + str
print(not_string('school'))
print(not_string('parrot'))
print(not_string('not working'))
