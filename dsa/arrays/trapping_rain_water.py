# Problem: Calculate how much rain water is trapped between walls
# Interview Question: "Given wall heights, how much water gets collected?"
# LeetCode: #42

# Approach - Prefix & Suffix Max Arrays
# Time Complexity: O(n)
# Space Complexity: O(n)

def trap_rain_water(heights):
    if not heights:
        return 0

    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n

    # Build left max array
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    # Build right max array
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])

    # Calculate water at each position
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - heights[i]

    return water

# Test
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"Heights: {heights}")
print(f"Total water trapped: {trap_rain_water(heights)} units")  # 6
