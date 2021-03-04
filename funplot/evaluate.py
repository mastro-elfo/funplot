from math import *


def evaluate(func, x, upper_limit, lower_limit):
    """Evaluate func in x with given boundaries"""
    try:
        # Try to evaluate func in x
        y = eval(func)
        # Check if y exceedes limits
        if y > upper_limit:
            return float("inf")
        elif y < lower_limit:
            return float("-inf")
        else:
            return y
    except:
        return nan
