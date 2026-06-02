# Problem: Insert a new node at the beginning
# Interview Question: "Add node at head of linked list"
# Input:  2 -> 3 -> 4, insert 1
# Output: 1 -> 2 -> 3 -> 4

# Approach - Update Head
# Time Complexity: O(1)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, value):
    new_node = Node(value)  # Create new node
    new_node.next = head    # Point to old head
    return new_node         # New node becomes new head

# Test
head = Node(2)
head.next = Node(3)
head.next.next = Node(4)

head = insert_at_beginning(head, 1)
curr = head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 3 -> 4
