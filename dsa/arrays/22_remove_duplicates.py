# Problem: Remove duplicates but keep original order
# Interview Question: "Clean the list — no repeats, same order"

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(n)
def remove_duplicates_brute(numbers):
    seen = []
    result = []
    for num in numbers:
        if num not in seen:
            seen.append(num)
            result.append(num)
    return result

# Optimal Approach - HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)
def remove_duplicates(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

# Test
nums = [4, 3, 2, 4, 1, 3, 5, 2]
print(f"Original: {nums}")
print(f"Brute Force: {remove_duplicates_brute(nums)}")
print(f"Optimal: {remove_duplicates(nums)}")
