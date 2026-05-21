# Problem: Find maximum in every window of size k
# Interview Question: "As a window slides across the list, what is max each time?"
# LeetCode: #239

# Brute Force Approach
# Time Complexity: O(n*k)
# Space Complexity: O(n)
def sliding_window_max_brute(numbers, k):
    result = []
    for i in range(len(numbers) - k + 1):
        window = numbers[i:i + k]
        result.append(max(window))
    return result

# Optimal Approach - Deque
# Time Complexity: O(n)
# Space Complexity: O(k)
from collections import deque
def sliding_window_max(numbers, k):
    result = []
    dq = deque()  # Stores indices
    for i, num in enumerate(numbers):
        # Remove elements outside window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller elements
        while dq and numbers[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(numbers[dq[0]])
    return result

# Test
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(f"List: {nums}")
print(f"Brute Force: {sliding_window_max_brute(nums, k)}")
print(f"Optimal: {sliding_window_max(nums, k)}")
