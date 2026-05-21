# Problem: Count how many times a value appears in linked list
# Interview Question: "Count occurrences of a value in linked list"
# Input:  1 -> 2 -> 2 -> 3 -> 2, value = 2
# Output: 3

# Approach - Single Pass
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_occurrences(head, value):
    count = 0
    curr = head

    while curr is not None:
        if curr.data == value:
            count += 1
        curr = curr.next

    return count

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(2)

print(count_occurrences(head, 2))  # 3
