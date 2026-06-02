# Problem: Count total number of nodes
# Interview Question: "Find length of linked list"
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 5

# Approach - Single Pass
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_length(head):
    count = 0
    curr = head

    while curr is not None:
        count += 1
        curr = curr.next

    return count

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(find_length(head))  # 5
