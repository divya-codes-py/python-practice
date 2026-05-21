# Problem: Find element that appears more than n/2 times
# Interview Question: "Which number dominates the list?"
# LeetCode: #169

# HashMap Approach
# Time Complexity: O(n)
# Space Complexity: O(n)
def find_majority_hashmap(numbers):
    count_map = {}
    for num in numbers:
        count_map[num] = count_map.get(num, 0) + 1
    majority = len(numbers) // 2
    for num, count in count_map.items():
        if count > majority:
            return num
    return None

# Optimal Approach - Boyer-Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_majority(numbers):
    candidate = None
    count = 0
    for num in numbers:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

# Test
nums = [3, 3, 4, 2, 3, 3, 3]
print(f"List: {nums}")
print(f"HashMap: {find_majority_hashmap(nums)}")
print(f"Optimal: {find_majority(nums)}")
