#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer. The factorial
        of a number n is the product of all positive integers less than or equal
        to n. This function uses a recursive approach.

    Parameters:
        n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial of the integer n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read an integer from command line argument, calculate its factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
