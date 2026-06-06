# Problem: Check if brackets are valid/balanced
# Interview Question: "Check if parentheses are balanced"
# Input:  "({[]})"  → True
# Input:  "({[})"   → False
# LeetCode: #20

# Approach - Stack + HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

def valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)  # Opening bracket — push
        else:
            if not stack or stack[-1] != mapping[char]:
                return False    # Mismatch!
            stack.pop()         # Matching bracket found

    return len(stack) == 0  # True if all matched

# Test
print(valid_parentheses("({[]})"))  # True
print(valid_parentheses("({[})"))   # False
print(valid_parentheses("()[]{}"))  # True
