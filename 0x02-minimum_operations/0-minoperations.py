#!/usr/bin/python3
""" writes a method called minOperations """


def minOperations(n):
    """
        Args:
            n: the number of characters

        Return:
            If n is impossible to achieve, return 0
            else returns the min number of operations
    """
    if not isinstance(n, int):
        return 0
    num_ops = 0
    note_pad = 0
    content = 1
    while content < n:
        if note_pad == 0:
            note_pad += content
            content += note_pad
            num_ops += 2
        elif n - content > 0 and (n - content) % content == 0:
            note_pad += content
            content += note_pad
            num_ops += 2
        elif note_pad > 0:
            content += note_pad
            num_ops += 1

    return num_ops
