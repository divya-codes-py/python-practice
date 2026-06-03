# Problem: Remove duplicate values from sorted linked list
# Interview Question: "Clean duplicate nodes from sorted linked list"
# Input:  1 -> 1 -> 2 -> 3 -> 3
# Output: 1 -> 2 -> 3
# LeetCode: #83

# Approach - Single Pass
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    curr = head

    while curr is not None and curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next  # Skip duplicate
        else:
            curr = curr.next

    return head

# Test
head = Node(1)
head.next = Node(1)
head.next.next = Node(2)
head.next.next.next = Node(3)
head.next.next.next.next = Node(3)

result = remove_duplicates(head)
curr = result
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 3
