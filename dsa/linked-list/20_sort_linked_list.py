# Problem: Sort linked list in ascending order
# Interview Question: "Sort linked list using bubble sort"
# Input:  3 -> 1 -> 4 -> 2
# Output: 1 -> 2 -> 3 -> 4

# Approach - Bubble Sort
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sort_linked_list(head):
    if head is None:
        return head

    swapped = True
    while swapped:
        swapped = False
        curr = head
        while curr.next is not None:
            if curr.data > curr.next.data:
                # Swap data values
                curr.data, curr.next.data = curr.next.data, curr.data
                swapped = True
            curr = curr.next

    return head

# Test
head = Node(3)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(2)

result = sort_linked_list(head)
curr = result
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
# Output: 1 -> 2 -> 3 -> 4
