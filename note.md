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


