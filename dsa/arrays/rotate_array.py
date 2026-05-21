# Problem: Rotate array to the right by K steps
# Interview Question: "Rotate array in-place without extra space"
# LeetCode: #189

# Optimal Approach - Three Reversal Trick
# Time Complexity: O(n)
# Space Complexity: O(1)

def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle k larger than array length

    # Trick: Reverse 3 times to get rotated array
    nums.reverse()                  # Step 1: Reverse whole array
    nums[:k] = reversed(nums[:k])  # Step 2: Reverse first k elements
    nums[k:] = reversed(nums[k:])  # Step 3: Reverse remaining elements

    return nums

# Test
print(rotate_array([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(rotate_array([1, 2, 3], 1))         # [3, 1, 2]
