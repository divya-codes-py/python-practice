# Problem: Find minimum element in a rotated sorted list
# Interview Question: "List was sorted then rotated — find the smallest"
# LeetCode: #153

# Brute Force Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_min_rotated_brute(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

# Optimal Approach - Binary Search
# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_min_rotated(numbers):
    left, right = 0, len(numbers) - 1
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] > numbers[right]:
            left = mid + 1  # Min is in right half
        else:
            right = mid     # Min is in left half
    return numbers[left]

# Test
nums = [4, 5, 6, 7, 1, 2, 3]
print(f"Rotated list: {nums}")
print(f"Brute Force: {find_min_rotated_brute(nums)}")
print(f"Optimal: {find_min_rotated(nums)}")
