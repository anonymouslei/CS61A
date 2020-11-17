def curry2(f):
    """Return a curried version of the given two-argument function."""
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g


def uncurry2(g):
    """Return a two-argument version of the given curried funciton."""
    def f(x, y):
        return g(x)(y)
    return f


identity = lambda x: x
increment = lambda x: x + 1
square = lambda x: x * x
triple = lambda x: 3 * x


def compose1(h, g):
    def f(x):
        return h(g(x))
    return f


def make_repeater(h, n):
    g = identity
    while n > 0:
        g = compose1(h, g)
        n = n - 1
    return g


def make_repeater1(h, n):
    return accumulate(compose1, lambda x: x, n, lambda k: h)


def accumulate(combiner, base, n, f):
    total, k = base, 1
    while k <= n:
        total, k = combiner(total, f(k)), k+1
    return total

def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum

if __name__ == '__main__':
    # pow_curried = curry2(pow)
    # a = pow_curried(2)(5)
    # add_three = make_repeater1(increment, 3)
    # make_repeater1(square, 2)(5)
    print_sums(1)(3)(5)