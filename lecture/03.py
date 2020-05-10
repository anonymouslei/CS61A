#print
print(None)
print(print(1),print(2))

# Division
from operator import truediv, floordiv, mod
618/10
618//10
618%10
print(floordiv(618,10))
print(truediv(618,10))
print(mod(618,10))

# Dostrings, doctests, & default arguments
def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D.

    >>> quotient, remainder = divide_exact(618,10)
    >>> quotient
    61
    >>> remainder
    8
    """
    return floordiv(n,d), mod(n,d)

# conditional expressions
def absolute_value(x):
    '''Return the absolute value of x.

    >>> absolute_value(-3)
    3
    >>> absolute_value(0)
    0
    >>> absolute_value(3)
    3
    '''
    if x<0:
        return -x
    elif x==0:
        return 0
    else:
        return x