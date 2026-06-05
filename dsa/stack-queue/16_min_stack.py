# Problem: Stack that also returns minimum element in O(1)
# Interview Question: "Design stack with push, pop, get_min all in O(1)"
# LeetCode: #155

# Approach - Two Stacks
# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

class MinStack:
    def __init__(self):
        self.stack = []      # Main stack
        self.min_stack = []  # Tracks minimums

    def push(self, item):
        self.stack.append(item)
        # Push to min_stack if it's smallest so far
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if self.stack:
            item = self.stack.pop()
            if item == self.min_stack[-1]:
                self.min_stack.pop()  # Remove from min too
            return item

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]  # Current minimum

# Test
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(2)
print(ms.get_min())  # 2
ms.pop()
print(ms.get_min())  # 3
