# Problem: Find duplicate numbers in a list
# Interview Question: "Which numbers appear more than once?"
# LeetCode: #442

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(n)
def find_duplicates_brute(numbers):
    seen = []
    duplicates = []
    for num in numbers:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.append(num)
    return duplicates

# Optimal Approach - HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)
def find_duplicates(numbers):
    seen = set()
    duplicates = []
    for num in numbers:
        if num in seen:
            if num not in duplicates:
                duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

# Test
nums = [1, 2, 3, 2, 4, 3, 5]
print(f"List: {nums}")
print(f"Brute Force: {find_duplicates_brute(nums)}")
print(f"Optimal: {find_duplicates(nums)}")
