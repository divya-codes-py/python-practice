# Problem: Evaluate a postfix (Reverse Polish Notation) expression
# Interview Question: "Calculate result of postfix expression using stack"
# LeetCode: #150

# Approach - Stack
# Time Complexity: O(n)
# Space Complexity: O(n)

def evaluate_postfix(tokens):
    stack = []

    for token in tokens:
        if token not in ['+', '-', '*', '/']:
            stack.append(int(token))  # Push number
        else:
            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Truncate towards zero

    return stack[0]

# Test
tokens = ["2", "1", "+", "3", "*"]
print(f"Tokens: {tokens}")
print(f"Result: {evaluate_postfix(tokens)}")  # 9

tokens2 = ["4", "13", "5", "/", "+"]
print(f"Tokens: {tokens2}")
print(f"Result: {evaluate_postfix(tokens2)}")  # 6
