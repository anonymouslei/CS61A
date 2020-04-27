# function values
max
max(3,4)
f = max
max = 7
f(3,max)

# area function
def area():
    return 3.14*radius*radius
area()
radius=20
area()
radius=10
area()

#Name conflicts
from operator import add, mul
def square(square):
    return mul(square,square)
square(4)
# function square works, no error
