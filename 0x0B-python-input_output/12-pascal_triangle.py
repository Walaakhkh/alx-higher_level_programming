#!/usr/bin/python3
""" Pascal's Triangle module.
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        # Compute the values in the middle of the row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
