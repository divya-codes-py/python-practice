# Problem: Find the longest sequence of consecutive numbers
# Interview Question: "What is the longest run of back-to-back numbers?"
# LeetCode: #128

# Sorting Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def longest_consecutive_sort(numbers):
    if not numbers:
        return 0
    numbers = list(set(numbers))
    numbers.sort()
    longest = 1
    current = 1
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1] + 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1
    return longest

# Optimal Approach - HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)
def longest_consecutive(numbers):
    num_set = set(numbers)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:  # Start of sequence
            current = 1
            while num + current in num_set:
                current += 1
            longest = max(longest, current)
    return longest

# Test
nums = [100, 4, 200, 1, 3, 2]
print(f"List: {nums}")
print(f"Sorting Approach: {longest_consecutive_sort(nums)}")
print(f"Optimal: {longest_consecutive(nums)}")
