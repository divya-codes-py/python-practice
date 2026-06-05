# Celebrity Problem
# Time Complexity: O(n)
# Space Complexity: O(n) — Stack approach

def celebrity(matrix):
    n = len(matrix)
    stack = list(range(n))

    # Phase 1: Find candidate using stack
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if matrix[a][b] == 1:   # a knows b → a eliminated
            stack.append(b)
        else:                    # a doesn't know b → b eliminated
            stack.append(a)

    candidate = stack.pop()

    # Phase 2: Verify candidate
    for i in range(n):
        if i == candidate:
            continue
        if matrix[candidate][i] == 1 or matrix[i][candidate] == 0:
            return -1

    return candidate


# -------------------------------------------
# Optimized Version: O(1) Space (Two Pointer)
# -------------------------------------------
def celebrity_optimized(matrix):
    n = len(matrix)
    left, right = 0, n - 1

    # Phase 1: Find candidate
    while left < right:
        if matrix[left][right] == 1:
            left += 1       # left knows right → left eliminated
        else:
            right -= 1      # left doesn't know right → right eliminated

    candidate = left

    # Phase 2: Verify candidate
    for i in range(n):
        if i == candidate:
            continue
        if matrix[candidate][i] == 1 or matrix[i][candidate] == 0:
            return -1

    return candidate


# Test
matrix = [
    [0, 1, 1],
    [0, 0, 0],
    [0, 1, 0]
]

print("Stack approach  :", celebrity(matrix))           # 1
print("Two pointer     :", celebrity_optimized(matrix)) # 1
