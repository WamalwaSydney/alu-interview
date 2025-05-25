#!/usr/bin/python3
"""Rain water trapping algorithm module."""


def rain(walls):
    if not walls or len(walls) < 3:
        return 0

    n = len(walls)

    # Arrays to store maximum height to left and right of each position
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max array - maximum height from left up to each position
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max array - maximum height from right up to each position
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate total trapped water
    water_trapped = 0
    for i in range(n):
        # Water level is minimum of max heights on both sides
        water_level = min(left_max[i], right_max[i])
        # Add trapped water at this position
        if water_level > walls[i]:
            water_trapped += water_level - walls[i]

    return water_trapped

