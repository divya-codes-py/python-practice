# Problem: Delete a node with given value
# Interview Question: "Remove node by value from linked list"
# Input:  1 -> 2 -> 3 -> 4 -> 5, delete 3
# Output: 1 -> 2 -> 4 -> 5

# Approach - Single Pass
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_node(head, value):
    # If head itself has the value
    if head.data == value:
        return head.next

    curr = head
    while curr.next is not None:
        if curr.next.data == value:
            curr.next = curr.next.next  # Skip the node
            return head
        curr = curr.next

    return head

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = delete_node(head, 3)
curr = result
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 4 -> 5
