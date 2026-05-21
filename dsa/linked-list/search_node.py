# Problem: Check if a value exists in linked list
# Interview Question: "Search for a node in linked list"
# Input:  1 -> 2 -> 3 -> 4 -> 5, search 3
# Output: True

# Approach - Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def search_node(head, value):
    curr = head

    while curr is not None:
        if curr.data == value:
            return True   # Found!
        curr = curr.next

    return False  # Not found

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(search_node(head, 3))  # True
print(search_node(head, 9))  # False
