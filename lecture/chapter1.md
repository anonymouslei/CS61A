## chapter1.3
###choosing names
- Function names are lowercase, with words separatd by underscores.Descriptive names are encouraged.
- Parameter names are lowercase, with words separated by underscores. Single-word names are preferred.
## chapter1.4
### designing functions
- each function should have exactly one job. That job should be identifiable with a short name and characterizable in a single line of text. functions that perform multiple jobs in sequence should be divided into multiple functions.
- don't repeat yourself is a central tenet of software engineering.
### documentation

- docstings are conventionally triple quoted.
the first line describes the job of the function in one line.
The following lines can describe arguments and clarify the behavior of the function.
```python
def pressure(v,t,n):
    '''Compute the pressure in pascals of an ideal gas.
    Applies the ideal gas law:xxx
    v -- volume of gas,in cubic meters
    '''
```
when you call `help` with the name of a function as an argument,
you see its docstring(type `q` to quit python help).
The python docs include [docstring guidlines](https://www.python.org/dev/peps/pep-0257/)
that maintain consistency across different Python projects.

### testing
**Assertions**
```python
def fib_test():
    assert fib(2) ==1, 'The 2nd Fibonacci number should be 1.'
    assert fib(3) ==1, 'the 3rd Fibnacci numver should be 1'
```
when writing Python in files, rather than directly into the interpreter,
tests are typically written in the same file or a neighboring file with the suffic
`_texst.py`.

**Doctests**
Python provides a convenient method for placing simple tests directly in the docstring of a function.
The first line of docstring should contain a one-line description of the funciton,
followed by a blank line.
A detailed description of arguments and behavior may follow.
In addition, the docstring may include a sample interactive session that calls the function.
```python
def sum_naturals(n):
    '''Return the sum of the first n natural numbers.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    '''
    total,k = 0,1
    while k<=n:
        total,k = total+k,k+1
    return total

from doctest import testmod
testmod()
```
[doctest module](https://docs.python.org/3/library/doctest.html)

To verify the doctest interactions for only a single function,
we use a `doctest` function called `run_docstring_examples`.
Its first argument is the function to test.
The second should always be the result of the expression `globals()`,
a build-in function that returns the global environment.
The third argument is `True` to indicate that we would like "verbose" output:
a catalog of all tests run.
```python
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
```

When writing Python in files,
all doctests in a file can be run by starting Python with
the doctest command line option:
```python
python3 -m doctest <python_source_file>
```
A test that applies a single function is called a _unit_ test.
Exhaustive unit testing is a hanllmark of good program design.