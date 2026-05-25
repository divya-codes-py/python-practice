# Maximum of Minimum for Every Window Size
# LeetCode style — O(n) Time | O(n) Space

def max_of_min(arr):
    n = len(arr)

    # Step 1: Previous smaller element index
    left = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    # Step 2: Next smaller element index
    right = [n] * n
    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # Step 3: Each element is minimum for windows of this length
    result = [0] * (n + 2)
    for i in range(n):
        length = right[i] - left[i] - 1
        result[length] = max(result[length], arr[i])

    # Step 4: Larger windows can't have bigger max-of-min
    # Propagate answer downward
    for i in range(n - 1, 0, -1):
        result[i] = max(result[i], result[i + 1])

    return result[1 : n + 1]


# Test
arr = [10, 20, 30, 50, 10, 70, 30]
ans = max_of_min(arr)

for size, val in enumerate(ans, 1):
    print(f"Window size {size} → {val}")
