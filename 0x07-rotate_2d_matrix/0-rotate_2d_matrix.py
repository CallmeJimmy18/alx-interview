#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return

    if not all(map(lambda x: type(x) == list, matrix)):
        return

    rws = len(matrix)
    cls = len(matrix[0])

    if not all(map(lambda x: len(x) == cls, matrix)):
        return

    c, r = 0, rws - 1
    for i in range(cls * rws):
        if i % rws == 0:
            matrix.append([])
        if r == -1:
            r = rws - 1
            c += 1
        matrix[-1].append(matrix[r][c])
        if c == cls - 1 and r >= -1:
            matrix.pop(r)
        r -= 1
