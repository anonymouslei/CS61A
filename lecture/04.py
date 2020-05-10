def same_length(a,b):
    """Return whether positive integers a and b have the same numver of digits.

    >>> same_length(50,70)
    True
    >>> same_length(50,100)
    False
    >>> same_length(1000, 1000000)
    False
    """

    return digits(a) == digits(b)


def digits(a):
    a_digits = 0
    while a>0:
        a = a //10
        a_digits = a_digits+1
    return a_digits


# functions as arguments

def sum_naturals(n):
    """sum the first N natural numbers

    >>> sum_naturals(5)
    15
    """
    total, k = 0,1
    while k<=n:
        total,k = total+k, k+1
    return total

def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    total,k = 0,1
    while k<=n:
        total, k = total+pow(k,3), k+1
    return total

def identity(k):
    return k

def cube(k):
    return pow(k,3)

def summation(n, term):
    """Sum the first N terms of a sequence.

    >>> summation(5, cube)
    255
    """
    total, k = 0,1
    while k<=n:
        total, k = total + term(k), k+1
    return total

from operator import mul

def pi_term(k):
    return 8 / mul(k*4-3, k*4-1)

summation(1000000, pi_term)


# local function definitions; returning functions

def make_adder(n):
    """Return a function that takes one argument K and returns k+N


    :param n:
    :return:
    """

