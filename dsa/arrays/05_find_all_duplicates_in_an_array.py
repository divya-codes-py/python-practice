# Problem: Find duplicate numbers in a list
# Interview Question: "Which numbers appear more than once?"
# LeetCode: #442

# Brute Force Approach - Nested Loops
# Time Complexity: O(n²)
# Space Complexity: O(n)
def find_duplicates_brute(numbers):
    duplicates = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                duplicates.add(numbers[i])
    return list(duplicates)


# Optimal Approach - HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)
def find_duplicates(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


# Best Approach - Index Marking (LC #442 constraint: 1 <= nums[i] <= n)
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_duplicates_optimal(numbers):
    numbers = numbers[:]  # copy to avoid mutating input
    duplicates = []
    for num in numbers:
        idx = abs(num) - 1
        if numbers[idx] < 0:
            duplicates.append(abs(num))
        else:
            numbers[idx] *= -1
    return duplicates


# Tests
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(f"List: {nums}")
print(f"Brute Force: {find_duplicates_brute(nums)}")   # [2, 3]
print(f"HashSet:     {find_duplicates(nums)}")          # [2, 3]
print(f"Optimal:     {find_duplicates_optimal(nums)}")  # [2, 3]
