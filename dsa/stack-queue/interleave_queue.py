# Interleave Queue
# Time Complexity: O(n)
# Space Complexity: O(n/2)

from collections import deque

def interleave_queue(q):
    # Edge case: must be even length
    if len(q) % 2 != 0:
        print("Queue must have even number of elements!")
        return q

    if len(q) == 0:
        return q

    half = len(q) // 2
    first_half = deque()

    # Phase 1: Separate first half
    for _ in range(half):
        first_half.append(q.popleft())
    # q now has only second half

    # Phase 2: Interleave first and second half
    while first_half:
        q.append(first_half.popleft())  # from first half
        q.append(q.popleft())           # from second half

    return q


# Tests
print(interleave_queue(deque([1,2,3,4])))       # [1,3,2,4]
print(interleave_queue(deque([1,2,3,4,5,6])))   # [1,4,2,5,3,6]
print(interleave_queue(deque([1,2,3])))          # odd → warning
print(interleave_queue(deque([])))               # empty → []
