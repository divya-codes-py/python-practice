# Problem: Climbing Stairs
# Interview Question: "How many ways to climb n stairs taking 1 or 2 steps?"
# LeetCode: #70

# Optimal Approach - Dynamic Programming (Fibonacci)
# Time Complexity: O(n)
# Space Complexity: O(1)

def climbStairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b  # Fibonacci pattern
    return b

# Test
print(f"2 stairs: {climbStairs(2)}")   # 2
print(f"3 stairs: {climbStairs(3)}")   # 3
print(f"5 stairs: {climbStairs(5)}")   # 8
