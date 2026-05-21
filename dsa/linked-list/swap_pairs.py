# Problem: Swap every two adjacent nodes
# Interview Question: "Swap nodes in pairs without modifying values"
# Input:  1 -> 2 -> 3 -> 4
# Output: 2 -> 1 -> 4 -> 3
# LeetCode: #24

# Approach - Dummy Node + Iterative
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    while prev.next is not None and prev.next.next is not None:
        first = prev.next
        second = prev.next.next

        # Swap the pair
        prev.next = second
        first.next = second.next
        second.next = first

        prev = first  # Move to next pair

    return dummy.next

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

result = swap_pairs(head)
curr = result
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 2 -> 1 -> 4 -> 3
