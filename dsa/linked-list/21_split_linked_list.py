# Problem: Split linked list into two equal halves
# Interview Question: "Split linked list using slow/fast pointer"
# Input:  1 -> 2 -> 3 -> 4
# Output: First: 1 -> 2, Second: 3 -> 4

# Approach - Fast & Slow Pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def split_linked_list(head):
    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:
        prev = slow
        slow = slow.next        # Slow moves 1 step
        fast = fast.next.next   # Fast moves 2 steps

    if prev:
        prev.next = None  # End first half

    return head, slow  # First half, Second half

# Test
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

first, second = split_linked_list(head)

print("First half:")
curr = first
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next

print("\nSecond half:")
curr = second
while curr:
    print(curr.data, end=" -> ")
    curr = curr.next
