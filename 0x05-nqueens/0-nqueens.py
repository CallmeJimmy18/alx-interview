#!/usr/bin/python3
""" N Queens """
import sys


def nqueens(n, y, brd):
    """
        placing N chess queens on an N×N chessboard so
        that no two queens attack each other.

        Return: All possible solutions to
            placement, in list of lists form
    """
    for i in range(n):
        hld = 0
        for q in brd:
            if i == q[1]:
                hld = 1
                break

            if y - i == q[0] - q[1]:
                hld = 1
                break
            if i - q[1] == q[0] - y:
                hld = 1
                break
            if hld == 0:
                brd.append([y, i])
                if y != n - 1:
                    nqueens(n, y + 1, brd)
                else:
                    print(brd)
                del brd[-1]


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n, 0, [])


if __name__ == '__main__':
    main()
