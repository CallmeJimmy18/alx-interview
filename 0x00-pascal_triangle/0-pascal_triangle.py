#!/usr/bin/python3
""" This is a pythin algorithm of pascal's triangle """


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for rows in range(n):
        row = [None] * (rows + 1)
        row[0], row[-1] = 1, 1
        for k in range(1, len(row) - 1):
            # Calculate the middle elements of each row
            row[k] = triangle[rows - 1][k - 1] + triangle[rows - 1][k]
        triangle.append(row)

    return triangle
