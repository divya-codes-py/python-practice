# Problem: Find two numbers that add up to a target
# Interview Question: "Return indices of two numbers that sum to target"
# LeetCode: #1 Two Sum

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(1)
def two_sum_brute(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return []

# Optimal Approach - HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
nums = [2, 7, 11, 15]
target = 9
print(f"List: {nums}")
print(f"Target: {target}")
print(f"Brute Force: {two_sum_brute(nums, target)}")
print(f"Optimal: {two_sum(nums, target)}")
