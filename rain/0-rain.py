#!/usr/bin/python3
"""
Module for calculating rainwater trapped between walls.

This module contains a function to calculate the amount of rainwater
that can be trapped between walls of different heights.

The main function 'rain' takes a list of non-negative integers representing
wall heights and returns the total units of water that would be retained
after rainfall.
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.

    Given a list of non-negative integers representing the heights of walls
    with unit width 1, calculate how much rainwater will be trapped.

    Args:
        walls (list): List of non-negative integers representing wall heights

    Returns:
        int: Total amount of rainwater retained in square units
    """
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


if __name__ == "__main__":
    test_cases = [
        [],
        [2, 0, 2],
        [0, 1, 0, 2, 0, 3, 0, 4],
        [1, 1, 2, 0, 1, 1, 1],
        [0, 2, 1, 0, 1, 3, 1, 2, 1, 1, 2, 1],
        [2, 0, 0, 0, 0, 3, 0],
        [1],
        [3, 3]
    ]

    expected_outputs = [0, 2, 6, 1, 6, 10, 0, 0]

    print("Running all test cases:")
    print("-" * 40)

    for i, walls in enumerate(test_cases):
        result = rain(walls)
        expected = expected_outputs[i]
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {walls}")
        print(f"Result: {result}, Expected: {expected} {status}")
        print()

    print("All tests completed!")
