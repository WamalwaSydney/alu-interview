#!/usr/bin/python3
"""
Module for calculating minimum operations to achieve n 'H' characters.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in
    exactly n 'H' characters in the file.

    Args:
        n (int): The target number of 'H' characters

    Returns:
        int: The minimum number of operations, or 0 if n is impossible
        to achieve
    """
    # If n is 1, we already have 'H', so no operations needed
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Find the sum of all prime factors of n
    while divisor <= n:
        # If n is divisible by divisor
        while n % divisor == 0:
            # Add the divisor to the number of operations
            operations += divisor
            # Divide n by divisor
            n //= divisor
        # Move to next potential divisor
        divisor += 1

    return operations


if __name__ == "__main__":
    # Test cases
    test_cases = [4, 12, 9]
    for n in test_cases:
        print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
