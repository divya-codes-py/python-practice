# Problem: Remove the Nth node from end of list
# Interview Question: "Delete Nth node from end in one pass"
# Input:  1 -> 2 -> 3 -> 4 -> 5, N = 2
# Output: 1 -> 2 -> 3 -> 5
# LeetCode: #19

# Approach - Two Pointer (Fast & Slow)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    fast = dummy
    slow = dummy

    # Move fast N+1 steps ahead
    for i in range(n + 1):
        fast = fast.next

    # Move both until fast reaches end
    while fast is not None:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next  # Remove the node
    return dummy.next

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = remove_nth_from_end(head, 2)
curr = result
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 3 -> 5
