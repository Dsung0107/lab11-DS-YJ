import math
<<<<<<< HEAD

def add(a, b):
    return a + b
=======
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Divide by zero")
    return b / a
def logarithm(a,b):
    if b <= 0:
        raise ValueError("Logarithm of non-positive number")
    return math.log(a, b)
def exponent(a,b):
    return a ** b


