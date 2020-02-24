"""
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. 
pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""

# Method 1
def pos_neg(a, b, negative):
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a<0 and b>0 )or (a>0 and b<0))
print(pos_neg(1,-1,False))
print(pos_neg(-1,1,False))
print(pos_neg(-4,-5,True))


"""
All comparison operators in Python have the same precedence. In addition, Python does chained comparisons. Thus,

(a < 0 != b < 0)
breaks down as:

(a < 0) and (0 != b) and (b < 0)
If any one of these is false, the total result of the expression will be False.

What you want to do is evaluate each condition separately, like so:

(a < 0) != (b < 0)
Other variants, from comments:

(a < 0) is not (b < 0) # True and False are singletons so identity-comparison works

(a < 0) ^ (b < 0) # bitwise-xor does too, as long as both sides are boolean

(a ^ b < 0) # or you could directly bitwise-xor the integers; 
            # the sign bit will only be set if your condition holds
            # this one fails when you mix ints and floats though

(a * b < 0) # perhaps most straightforward, just multiply them and check the sign

"""

# Method 2
def pos_neg(a, b, negative):
    return ((a<0 and b<0) if negative else a<0 and b>0 or (a>0 and b<0))
print(pos_neg(1,-1,False))
print(pos_neg(-1,1,False))
print(pos_neg(-4,-5,True))
