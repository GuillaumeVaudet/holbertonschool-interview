#!/usr/bin/python3
"""First exercice of algorithm in Holberton cursus"""


def pascal_triangle(n):
    """Function that returns a list of lists representing Pascal's traingle"""

    if n <= 0:
        return []

    first_list = [1]
    pascal_list = []

    pascal_list.append(first_list)

    for i in range(1, n):
        old_list = pascal_list[-1]
        new_list = [1]

        for j in range(1, i):
            new_list.append(old_list[j-1] + old_list[j])

        new_list.append(1)
        pascal_list.append(new_list)

    return pascal_list
