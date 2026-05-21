# Problem: Reverse a linked list
# Interview Question: "Reverse linked list in-place"
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1
# LeetCode: #206

# Optimal Approach - Three Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next  # Save next node
        curr.next = prev       # Reverse the pointer
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward

    return prev  # New head

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = reverse_linked_list(head)
curr = result
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 5 -> 4 -> 3 -> 2 -> 1
