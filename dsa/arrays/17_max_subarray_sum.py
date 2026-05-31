# Problem: Find subarray with the largest sum
# Interview Question: "Which continuous portion of the list has the biggest total?"
# LeetCode: #53

# Optimal Approach - Kadane's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

def max_subarray_sum(numbers):
    max_sum = numbers[0]
    current_sum = numbers[0]

    for num in numbers[1:]:
        # Either extend current subarray or start fresh
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"List: {nums}")
print(f"Maximum subarray sum: {max_subarray_sum(nums)}")  # 6
