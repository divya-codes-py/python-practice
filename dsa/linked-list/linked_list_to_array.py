# Problem: Convert linked list to Python list
# Interview Question: "Convert linked list to array"
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: [1, 2, 3, 4, 5]

# Approach - Single Pass
# Time Complexity: O(n)
# Space Complexity: O(n)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linked_list_to_array(head):
    result = []
    curr = head

    while curr is not None:
        result.append(curr.data)
        curr = curr.next

    return result

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print(linked_list_to_array(head))  # [1, 2, 3, 4, 5]
