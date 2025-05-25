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


if __name__ == "__main__":
    """Test the rain function with various test cases."""
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

    expected_outputs = [0, 2, 6, 1, 7, 8, 0, 0]

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
