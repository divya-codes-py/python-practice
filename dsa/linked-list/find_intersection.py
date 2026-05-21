# Problem: Find where two linked lists meet
# Interview Question: "Find intersection node of two linked lists"
# LeetCode: #160

# Approach - HashSet
# Time Complexity: O(n + m)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_intersection(head1, head2):
    visited = set()

    # Store all nodes of first list
    curr = head1
    while curr is not None:
        visited.add(curr)
        curr = curr.next

    # Check second list nodes
    curr = head2
    while curr is not None:
        if curr in visited:
            return curr.data  # Intersection found!
        curr = curr.next

    return None  # No intersection

# Test
common = Node(8)
common.next = Node(10)

head1 = Node(1)
head1.next = Node(2)
head1.next.next = common

head2 = Node(5)
head2.next = common

print(find_intersection(head1, head2))  # 8
