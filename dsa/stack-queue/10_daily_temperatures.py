# Problem: Find how many days until warmer temperature
# Interview Question: "For each day, how many days to wait for warmer weather?"
# LeetCode: #739

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(n)
def daily_temperatures_brute(temperatures):
    result = [0] * len(temperatures)
    for i in range(len(temperatures)):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break
    return result

# Optimal Approach - Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # Stores indices

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            idx = stack.pop()
            result[idx] = i - idx  # Days waited
        stack.append(i)

    return result

# Test
temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(f"Temperatures: {temps}")
print(f"Brute Force: {daily_temperatures_brute(temps)}")
print(f"Optimal: {daily_temperatures(temps)}")
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
