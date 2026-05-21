# Problem: Check if linked list reads same forwards and backwards
# Interview Question: "Is the linked list a palindrome?"
# Input:  1 -> 2 -> 3 -> 2 -> 1
# Output: True

# Approach - Store values in list
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def is_palindrome(head):
    values = []
    curr = head

    while curr is not None:
        values.append(curr.data)
        curr = curr.next

    return values == values[::-1]  # Compare with reverse

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
print(is_palindrome(head))   # True

head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
print(is_palindrome(head2))  # False
