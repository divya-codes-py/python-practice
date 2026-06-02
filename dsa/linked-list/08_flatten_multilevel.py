# Problem: Linked list has next and child pointers, flatten it
# Interview Question: "Flatten multilevel linked list into single level"
# Input:  1 -> 2 -> 3
#              |
#              4 -> 5
# Output: 1 -> 2 -> 4 -> 5 -> 3
# LeetCode: #430

# Approach - Iterative
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None

def flatten(head):
    curr = head

    while curr is not None:
        if curr.child is not None:
            child = curr.child
            next_node = curr.next

            curr.next = child   # Connect child
            curr.child = None   # Remove child pointer

            # Find end of child list
            temp = child
            while temp.next is not None:
                temp = temp.next

            temp.next = next_node  # Connect back to next

        curr = curr.next

    return head

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.child = Node(4)
head.next.child.next = Node(5)

result = flatten(head)
curr = result
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 4 -> 5 -> 3
