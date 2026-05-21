# Problem: Find the second largest number in the array
# Interview Question: "Find second largest without sorting"
# Input:  [10, 20, 4, 45, 99]
# Output: 45

# Optimal Approach - Single Pass
# Time Complexity: O(n)
# Space Complexity: O(1)

def second_largest(nums):
    if len(nums) < 2:
        return None

    first = float('-inf')   # Largest number so far
    second = float('-inf')  # Second largest so far

    for num in nums:
        if num > first:
            second = first  # Old largest becomes second
            first = num     # New largest found
        elif num > second and num != first:
            second = num    # New second largest found

    return second

# Test
print(second_largest([10, 20, 4, 45, 99]))  # 45
print(second_largest([5, 5, 4, 3]))          # 4
print(second_largest([1, 1]))                # -inf (no second)
