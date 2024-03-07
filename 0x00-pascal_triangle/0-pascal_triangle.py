#!/usr/bin/python3
""" This is a pythin algorithm of pascal's triangle """


def pascal_triangle(n):
    triangle = []

    if n <= 0:
        return []
    for rows in range(n):
        row = [None for i in range(rows + 1)]
        row[0], row[-1] = 1, 1
        for k in range(1, len(row) - 1):
            row[k] = triangle[rows - 1][k - 1] + triangle[rows - 1][k]
        triangle.append(row)

    return triangle
