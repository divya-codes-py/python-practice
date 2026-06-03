# Problem: Move all zeros to the end, keep order of other elements
# Interview Question: "Move zeros to end without changing order of other elements"
# LeetCode: #283

# Optimal Approach - Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

def move_zeros(nums):
    # Position where next non-zero number should go
    insert_pos = 0

    # Step 1: Move all non-zero numbers to the front
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # Step 2: Fill remaining positions with zeros
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

    return nums

# Test
print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeros([0, 0, 1]))         # [1, 0, 0]
