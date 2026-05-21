# Problem: Print linked list values in reverse order
# Interview Question: "Print linked list backwards without reversing it"
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 5 4 3 2 1

# Approach - Store then Reverse
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_reverse(head):
    values = []
    curr = head

    while curr is not None:
        values.append(curr.data)
        curr = curr.next

    for val in reversed(values):  # Print in reverse
        print(val, end=" ")

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print_reverse(head)  # 5 4 3 2 1
