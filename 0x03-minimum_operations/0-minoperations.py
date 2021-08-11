#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed to
result in exactly n H characters in the file.
args:
  n: number of times that the letter repeats
"""


def minOperations(n):
    """minimum of operation"""
    if n < 2 or type(n) is not int:
        return 0
    letters = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while (n % i == 0 and n != 1):
                n = n / i
                letters.append(i)
    return sum(letters)
