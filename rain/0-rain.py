#!/usr/bin/python3
"""Rain water trapping algorithm module."""


def rain(walls):
    """Calculates the total amount of rainwater trapped between walls."""
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    water_trapped = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level > walls[i]:
            water_trapped += water_level - walls[i]

    return water_trapped
