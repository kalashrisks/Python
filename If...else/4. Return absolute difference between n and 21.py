# Given an int n, return the absolute difference between n and 21 except return double the absolute difference if n is over 21
def diff21(n):
    if n > 21:
        result = 2 * (n -21)
    else:
        result = 21 - n
    return result


print(diff21(19))
print(diff21(21))
print(diff21(10))
