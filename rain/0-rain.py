#!/usr/bin/python3
"""
Rain water trapping problem solution
"""


def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.
    
    Args:
        walls: List of non-negative integers representing wall heights
        
    Returns:
        Integer indicating total amount of rainwater retained
    """
    if not walls or len(walls) < 3:
        return 0
    
    n = len(walls)
    
    # Arrays to store the maximum height to the left and right of each position
    left_max = [0] * n
    right_max = [0] * n
    
    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])
    
    # Fill right_max array
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])
    
    # Calculate trapped water
    water_trapped = 0
    for i in range(n):
        # Water level at position i is minimum of max heights on both sides
        water_level = min(left_max[i], right_max[i])
        # Water trapped is the difference between water level and wall height
        if water_level > walls[i]:
            water_trapped += water_level - walls[i]
    
    return water_trapped


# Test the function with the provided examples
if __name__ == "__main__":
    # Test case 1: [0, 1, 0, 2, 0, 3, 0, 4]
    walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
    result1 = rain(walls1)
    print(f"Test 1 - walls: {walls1}")
    print(f"Water trapped: {result1}")
    print()
    
    # Test case 2: [2, 0, 0, 4, 0, 0, 1, 0]
    walls2 = [2, 0, 0, 4, 0, 0, 1, 0]
    result2 = rain(walls2)
    print(f"Test 2 - walls: {walls2}")
    print(f"Water trapped: {result2}")
    print()
    
    # Additional test cases
    print("Additional test cases:")
    
    # Empty list
    print(f"Empty list: {rain([])}")
    
    # Single wall
    print(f"Single wall [5]: {rain([5])}")
    
    # Two walls
    print(f"Two walls [3, 1]: {rain([3, 1])}")
    
    # No water can be trapped
    print(f"Ascending [1, 2, 3, 4]: {rain([1, 2, 3, 4])}")
    
    # Classic example
    print(f"Classic [3, 0, 2, 0, 4]: {rain([3, 0, 2, 0, 4])}")
