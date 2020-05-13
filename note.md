##01.py
- set 关键字，只保存不可重复的关键字的容器
- {w for w in words if w==w[::-1] and len(w)>4}

## hw01.py
- the name of the function can also be assigned.
    e.g. `h=add  return h(a,b)`
- if function uses a call expression(func(c(t),t(),f()), it guarantees that all of its operand subexpressions will be evaluated before func runs inside.

## chapter1.3
- function names are lowercase, with word separated by underscores, Descriptive names are encouraged.
- parameter names are lowercase, with words separated by underscores. Single word names are preferred.

## chapter1.4
### designing functions
- each function should have exactly one job. That job should be identifiable with a short name and characterizable in a single line of text. functions that perform multiple jobs in sequence should be divided into multiple funcitons.

### documentation
- docstings are conventionally triple quoted
the first line describes the job of the function in one line.
The following lines can describe arguments and clarify the behavior of the function

## chapter1.5 Contorl
### Boolean Operators
- **and** stops evaluating any more expressions once it reaches the first false value and returns it.
If all values evaluate to a true value,
the last value is returned
- **or** short-circuits at the first true value and returns it. If all values evaluate to a false value,
the last value is returned.

### testing
- **assertions**
`assert fib(2)==1, 'the 2nd Fibonacci number should be 1'`
`assert fib(50) == 77213, 'Error at the 50th Fibonacci number'`

```python
def sum_naturals(n):
    """Return the sum of the first n natural numbers.
    
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
```
```python
>>> from doctest import testmod
>>> testmod()
```

```python
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
```
Its first argument is the function to test.
the second should always be the result of the expression `globals()`,
the third argument is `True` to indicate that we would like "verbose" output: a catalog of all tests run.

```commandline
python3 -m doctest <python_source_file>
```

## chapter 1.6 Higher-order Function
### Functions as arguments
```python
def summation(n, term):
    total, k = 0, 1
    while k<=n:
        total, k = total + term(k), k+1
    return total

def cube(x):
    return x*x*x

def sum_cubes(n):
    return summation(n, cube)

result = sum_cubes(3)

def identity(x):
    return x

def sum_naturals(n):
    return summation(n, identity)
```

###Functions as general methods
```python
def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def square_close_to_successor(guess):
    return approx_eq(guess*guess, guess+1)

def approx_eq(x,y,tolerance=1e-15):
    return abs(x-y)<tolerance

from math import sqrt
phi = 1/2 + sqrt(5)/2
def improve_test():
    approx_phi = improve(golden_update, square_close_to_successor)
    assert approx_eq(phi, approx_phi), 'phi differs from its approximation'

```
this example illustrates two related big ideas in computer science.
First, naming and functions allow us to abstract away a vast amount of complexity.
While each function definition has been trivial,
the computational process set in motion by our evaluation procedure is quite intricate.
Second, it is only be virtue of the face that we have an extremely general evaluation procedure for the python language that small components can be composed into complex processes.

### Defining Funcitons: Nested definitions
one negative consequence of this approach is that the global frame becomes cluttered with names of small functions,
which must all be unique.
another problem is that we are constrained by partivular funciton signatures:
the `update` argument to `improve` must take exactly one argument.
Nested funciton definitions address both of these problems,
but require us to enrich our environment model.
```python
def sqrt(a):
    def sqrt_update(x):
        return average(x, a/x)
    def sqrt_close(x):
        return approx_eq(x*x, a)
    return improve(sqrt_update, sqrt_close)
```
we require two extensions to our environment model to enable lexical scoping.
1. each user-defined function has a parent environment in which it was defined.
2. when a user-defined is called, its local frame extends its parent environment.

Hence, we realize two key advantages of lexical scoping in Python.
- the names of a local function do not interfere with names external to the function in which it is defined,
because the local function name will be bound in the current local environment in which it was defined,
rather than the global environment.
- A local function can access the environment of the enclosing function,
because the enclosing function,
because the body of the local function is evaluated in an environment that extends the evaluation environment in which it was defined.

locally defined functions are often called `closures`

### functions as returned values
An important feature of lexically scoped programming languages is that locally defined functions maintain their parent environment
when they are returned.
```python
def square(x):
    return x*x

def successor(x):
    return x+1

def compose1(f,g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    """Never called."""
    return -x

square_successor = compose1(square, successor)
result = square_successor(12)
```
### Example: Newton's Method
Newton's method is an iterative improvement algorithm:
it improves a guess of the zero for any function that id differentiable,
which means that it can be approximated by a straight line at any point.
Newton's method follows these linear approximations to find function zeros.

A newton_update expresses the computational process of following this tangent line to 0,
for a function f and its derivative df.
```python
def newton_update(f, df):
    def update(x):
        return x-f(x)/df(x)
    return update

def find_zero(f, df):
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update(f, df), near_zero)

def square_root(a):
    def f(x):
        return x*x - a
    def df(x):
        return 2*x
    return find_zero(f,df)

def power(x, n):
    product, k = 1, 0
    while k < n:
        product, k = product * x, k+ 1
    return product

def root(n, a):
    def f(x):
        return power(x, n) - a
    def df(x):
        return n * power(x, n-1)
    return find_zero(f, df)
```
as you experiment with Newton's method,
be aware that it will not always converge.
The initial guess of `improve` must be sufficiently close to the zero,
and various conditions about the funciton must be met.
Despite this shortcoming,
Newton's method is a powerful general computational method for solving differentiable equations.
very fast algorithms for logarithms and large integer division employ variants of the technique in modern computers.

### currying 
We can use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each takes a single argument.
This transformation is called currying.
In python,
currying is useful when we require a function that takes in only a single argument.
For example, the map pattern applies a single-argument function to sequence of values.
```python
def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1

map_to_range(0, 10, curried_pow(2))

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


if __name__ == '__main__':
    pow_curried = curry2(pow)
    a = pow_curried(2)(5)
    map_to_range(0, 10, pow_curried(2))
```
the curry2 function takes in a two-argument function `f` and returns a single-argument function
`g`.
When `g` is applied to an argument `x`, it returns a single-argument funciton `h`.
When `h` is applied to `y`,
it calls `f(x, y)`.
Thus, `curry2(f)(x)(y)` is equivalent to `f(x, y)`.
Then `uncurry2` function reverses the currying transformation,
so that `uncurry2(curry2(f))` is equivalent to `f`.

### lambda expressions
In python, we can create function values on the fly using `lambda` expressions,
which evaluate to unnamed function.
A lambda expression evaluates to a function that has a single return expression as its body.
Assignment and control statements are not allowed.

| lambda          | x      | :          | f(g(x)) |
| --------------- | ------ | ---------- | ------- |
|"a function that"| takes x| and returns| f(g(x)) |



## 05-Environments
Higher-order funciton:
- a function that takes a function as an argument value
- a function that returns a function as a return value

**lambda expressions**
- lambda expressions are not common in python, but important in general
- lambda expressions in python cannot contain statements at all!
```python
square = lambda x: x * x # lambda expressions
def square(x): # def statements
    return x * x 
```
VS:
- both create a function with the same domain, range and behavior
- both bind that function to the name square
- only the def statement gives the function an intrinsic name,
which shows up in environment diagrams but doesn't affect execution.