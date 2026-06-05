# Problem: Find span of stock prices for each day
# Interview Question: "How many consecutive days before today had lower/equal price?"
# LeetCode: #901

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(n)
def stock_span_brute(prices):
    n = len(prices)
    span = [1] * n
    for i in range(1, n):
        j = i - 1
        while j >= 0 and prices[j] <= prices[i]:
            span[i] += 1
            j -= 1
    return span

# Optimal Approach - Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def stock_span(prices):
    stack = []  # Stores indices
    span = [1] * len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        span[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    return span

# Test
prices = [100, 80, 60, 70, 60, 75, 85]
print(f"Prices: {prices}")
print(f"Brute Force: {stock_span_brute(prices)}")
print(f"Optimal: {stock_span(prices)}")
# Output: [1, 1, 1, 2, 1, 4, 6]
