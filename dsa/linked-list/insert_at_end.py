# Problem: Insert a new node at the end
# Interview Question: "Add node at tail of linked list"
# Input:  1 -> 2 -> 3, insert 4
# Output: 1 -> 2 -> 3 -> 4

# Approach - Traverse to End
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, value):
    new_node = Node(value)

    if head is None:
        return new_node  # Empty list, new node is head

    curr = head
    while curr.next is not None:
        curr = curr.next  # Go to last node

    curr.next = new_node  # Add at end
    return head

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

head = insert_at_end(head, 4)
curr = head
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 3 -> 4
