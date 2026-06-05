# Problem: Find next greater element for each number
# Interview Question: "For each element, find the first greater element to its right"
# LeetCode: #496

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(n)
def next_greater_brute(numbers):
    result = []
    for i in range(len(numbers)):
        found = False
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[i]:
                result.append(numbers[j])
                found = True
                break
        if not found:
            result.append(-1)
    return result

# Optimal Approach - Monotonic Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def next_greater(numbers):
    result = [-1] * len(numbers)
    stack = []  # Stores indices

    for i in range(len(numbers)):
        # Pop elements smaller than current
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            result[idx] = numbers[i]
        stack.append(i)

    return result

# Test
nums = [4, 5, 2, 10, 8]
print(f"List: {nums}")
print(f"Brute Force: {next_greater_brute(nums)}")
print(f"Optimal: {next_greater(nums)}")
# Output: [5, 10, 10, -1, -1]
