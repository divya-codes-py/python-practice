# Problem: Sort a stack in ascending order
# Interview Question: "Sort stack using only stack operations"

# Approach - Recursive
# Time Complexity: O(n²)
# Space Complexity: O(n)

def insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
        return

    top = stack.pop()
    insert_sorted(stack, element)
    stack.append(top)

def sort_stack(stack):
    if len(stack) <= 1:
        return

    top = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, top)

# Test
stack = [3, 1, 4, 2, 5]
print(f"Original: {stack}")
sort_stack(stack)
print(f"Sorted: {stack}")  # [1, 2, 3, 4, 5]
