# Problem: Find the Nth node from the end
# Interview Question: "Find Nth node from end in one pass"
# Input:  1 -> 2 -> 3 -> 4 -> 5, N = 2
# Output: 4

# Approach - Fast & Slow Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def nth_from_end(head, n):
    fast = head
    slow = head

    # Move fast pointer N steps ahead
    for i in range(n):
        if fast is None:
            return None
        fast = fast.next

    # Move both until fast reaches end
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow.data

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(nth_from_end(head, 2))  # 4
