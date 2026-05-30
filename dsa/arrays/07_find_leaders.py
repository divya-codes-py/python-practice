# Problem: Find all leaders (no element to the right is greater)
# Interview Question: "Which numbers are bigger than everything after them?"

# Optimal Approach - Right to Left Scan
# Time Complexity: O(n)
# Space Complexity: O(n)

def find_leaders(numbers):
    leaders = []
    max_from_right = numbers[-1]
    leaders.append(max_from_right)  # Rightmost is always a leader

    for i in range(len(numbers) - 2, -1, -1):
        if numbers[i] >= max_from_right:
            max_from_right = numbers[i]
            leaders.append(numbers[i])

    return leaders[::-1]  # Reverse to maintain original order

# Test
nums = [16, 17, 4, 3, 5, 2]
result = find_leaders(nums)
print(f"List: {nums}")
print(f"Leaders: {result}")  # [17, 5, 2]
