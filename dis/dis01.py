from doctest import run_docstring_examples


def wears_jacket_with_if(temp, raining):
    """

    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return raining or temp < 60


def is_prime(n):
    """

    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1)
    False
    """
    if n ==1:
        return False
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i = i+1
    return True

if __name__ == '__main__':
    run_docstring_examples(is_prime, globals(),True)
