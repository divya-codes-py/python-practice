# Problem: Check if linked list has a loop
# Interview Question: "Detect cycle in linked list"
# LeetCode: #141

# Approach - Floyd's Cycle Detection (Tortoise & Hare)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_loop(head):
    slow = head  # Moves 1 step
    fast = head  # Moves 2 steps

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # They met — loop exists!
            return True

    return False  # No loop

# Test - with loop
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2  # Loop created here
print(detect_loop(n1))  # True

# Test - without loop
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print(detect_loop(head))  # False
