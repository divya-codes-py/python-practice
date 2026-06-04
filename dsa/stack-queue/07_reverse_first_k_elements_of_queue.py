# Reverse First K Elements of Queue
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque

def reverse_k(q, k):
    # Edge cases
    if k <= 0 or k > len(q):
        return q

    stack = []

    # Step 1: Push first k elements into stack
    for _ in range(k):
        stack.append(q.popleft())

    # Step 2: Pop from stack and append back to queue
    while stack:
        q.append(stack.pop())

    # Step 3: Rotate remaining elements
    for _ in range(len(q) - k):
        q.append(q.popleft())

    return q


# Test
q = deque([1, 2, 3, 4, 5])
result = reverse_k(q, 3)

print(list(result))  # Output: [3, 2, 1, 4, 5]
