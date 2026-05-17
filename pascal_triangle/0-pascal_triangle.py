#!/usr/bin/env python3
"""First exercice of algorithm in Holberton cursus"""


def pascal_triangle(n):
    """Function that returns a list of lists representing Pascal's traingle"""

    if n <= 0:
        return []

    first_list = [1]
    pascal_list = []

    pascal_list.append(first_list)

    for i in range(1, n):
        past_list = pascal_list[-1]
        new_list = [1]

        for j in range(1, i):
            new_list.append(past_list[j-1] + past_list[j])

        new_list.append(1)
        pascal_list.append(new_list)

    return pascal_list


if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Print the triangle
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
