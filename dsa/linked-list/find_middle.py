# Problem: Find the middle element of linked list
# Interview Question: "Find middle node in one pass"
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 3
# LeetCode: #876

# Approach - Fast & Slow Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_middle(head):
    slow = head  # Moves 1 step
    fast = head  # Moves 2 steps

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.data  # slow is at middle

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(find_middle(head))  # 3
