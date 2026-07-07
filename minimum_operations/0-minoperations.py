#!/usr/bin/python3
"""
Module providing the minOperations function.

Computes the fewest number of Copy All / Paste operations needed
to obtain exactly n 'H' characters starting from a single one.
"""


def minOperations(n):
    """
    Compute the minimu number of operations to reach n characters.

    Args:
        n (int): The target number of characters.

    Returns:
        int: The minimum number of operations, or 0 if n is
        impossible to reach (n < 2)
    """
    total = 0
    d = 2
    if n < 2:
        return 0

    while n > 1:
        if n % d == 0:
            total = total + d
            n = n // d
        else:
            d = d + 1
    return total


if __name__ == "__main__":
    print(minOperations(4))
    print(minOperations(12))
