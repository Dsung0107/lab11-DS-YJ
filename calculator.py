#https://github.com/Dsung0107/lab11-DS-YJ.git
#Partner 1: Derek Sung
#Partner 2: Yoonho Ji

import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Divide by zero")
    return b / a
def log(a,b):
    if b <= 0:
        raise ValueError("Logarithm of non-positive number")
    return math.log(a, b)
def exp(a,b):
    return a ** b
def square_root(a):
    if a<0:
        raise ValueError("Square root of non-positive number")
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.hypot(a , b)



