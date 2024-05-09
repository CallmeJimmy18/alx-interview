#!/usr/bin/python3
"""perimeter of the island"""


def island_perimeter(grid):
    """Calculates the perimeter of an island
    """
    parim = 0
    if type(grid) != list:
        return 0

    l = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == l - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 row[j - 1] == 0,
            )
            parim += sum(edges)

    return parim
