#!/usr/bin/python3
"""Test runner for the rainwater trapping algorithm."""

import importlib.util
import os

# Load the 0-rain.py module dynamically
module_name = "rain"
module_path = os.path.join(os.path.dirname(__file__), "0-rain.py")
spec = importlib.util.spec_from_file_location(module_name, module_path)
rain_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rain_module)


def main():
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
        result = rain_module.rain(walls)
        expected = expected_outputs[i]
        status = "✓" if result == expected else "✗"
        print(f"Test {i + 1}: {walls}")
        print(f"Result: {result}, Expected: {expected} {status}\n")

    print("All tests completed!")


if __name__ == "__main__":
    main()

