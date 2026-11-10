# https://github.com/K-Nguyen-92/lab10-KN-OC
# Partner 1: Khoa Nguyen
# Partner 2: Octavia Chambers

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math


# First example
def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except ValueError:
        raise


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm input")
    return math.log(b, a)


def exp(a, b):
    return a**b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Log base 'a' must be positive and not equal 1")
    if b <= 0:
        raise ValueError("Log argument 'b' must be greater than 0")
    return math.log(b, a)


def exponent(a, b):
    return a**b
