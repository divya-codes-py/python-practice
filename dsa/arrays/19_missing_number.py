# Problem: Find missing number in list from 1 to n
# Interview Question: "One number is missing from 1 to n, find it"
# LeetCode: #268

# Optimal Approach - Math Formula
# Time Complexity: O(n)
# Space Complexity: O(1)

def find_missing(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2  # Sum formula: n*(n+1)/2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum

# Test
nums = [1, 2, 4, 5, 6]
result = find_missing(nums)
print(f"List: {nums}")
print(f"Missing number: {result}")
