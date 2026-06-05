# Problem: Build a Queue using only Stack operations
# Interview Question: "Implement Queue using two stacks"
# Input:  enqueue 1, 2, 3 → dequeue should give 1 first
# LeetCode: #232

# Approach - Two Stacks
# Enqueue: Time Complexity: O(1)
# Dequeue: Time Complexity: O(n) amortized O(1)
# Space Complexity: O(n)

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue
        self.stack2 = []  # For dequeue

    def enqueue(self, item):
        self.stack1.append(item)  # Always push to stack1

    def dequeue(self):
        if not self.stack2:
            # Move all items from stack1 to stack2
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return "Queue is empty!"

        return self.stack2.pop()  # Pop from stack2

# Test
q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # 1
print(q.dequeue())  # 2
q.enqueue(4)
print(q.dequeue())  # 3
