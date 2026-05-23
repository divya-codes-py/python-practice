# Problem: Find largest rectangle area in histogram
# Interview Question: "Find maximum area rectangle in histogram"
# LeetCode: #84

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(1)
def largest_rectangle_brute(heights):
    max_area = 0
    for i in range(len(heights)):
        min_height = heights[i]
        for j in range(i, len(heights)):
            min_height = min(min_height, heights[j])
            area = min_height * (j - i + 1)
            max_area = max(max_area, area)
    return max_area

# Optimal Approach - Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def largest_rectangle(heights):
    stack = []  # Stores indices
    max_area = 0
    heights.append(0)  # Sentinel value

    for i in range(len(heights)):
        while stack and heights[stack[-1]] >= heights[i]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    heights.pop()  # Remove sentinel
    return max_area

# Test
heights = [2, 1, 5, 6, 2, 3]
print(f"Heights: {heights}")
print(f"Brute Force: {largest_rectangle_brute(heights)}")
print(f"Optimal: {largest_rectangle(heights)}")
# Output: 10
