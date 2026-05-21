# Problem: Create a Stack with push, pop, peek operations
# Interview Question: "Implement Stack from scratch"
# Stack = Last In First Out (LIFO)

# All operations:
# Time Complexity: O(1)
# Space Complexity: O(n)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # O(1)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()  # O(1)

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]    # O(1)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Test
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())   # 30
print(s.pop())    # 30
print(s.pop())    # 20
print(s.size())   # 1
