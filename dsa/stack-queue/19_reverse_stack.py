# Problem: Reverse a stack using recursion
# Interview Question: "Reverse stack without using extra stack"

# Approach - Recursive
# Time Complexity: O(n²)
# Space Complexity: O(n)

def insert_bottom(stack, element):
    if not stack:
        stack.append(element)
        return

    top = stack.pop()
    insert_bottom(stack, element)
    stack.append(top)

def reverse_stack(stack):
    if len(stack) <= 1:
        return

    top = stack.pop()
    reverse_stack(stack)
    insert_bottom(stack, top)

# Test
stack = [1, 2, 3, 4, 5]
print(f"Original: {stack}")
reverse_stack(stack)
print(f"Reversed: {stack}")  # [5, 4, 3, 2, 1]
