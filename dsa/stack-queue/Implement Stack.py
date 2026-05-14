# Problem: Create a Stack with push, pop, peek operations
# Stack = Last In First Out (LIFO)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]

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
