# Problem: Count pairs where left element is greater than right
# Interview Question: "How many times is the list out of order?"

# Brute Force Approach
# Time Complexity: O(n²)
# Space Complexity: O(1)
def count_inversions_brute(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                count += 1
    return count

# Optimal Approach - Merge Sort
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def count_inversions(numbers):
    if len(numbers) <= 1:
        return numbers, 0
    mid = len(numbers) // 2
    left, left_count = count_inversions(numbers[:mid])
    right, right_count = count_inversions(numbers[mid:])
    merged = []
    count = left_count + right_count
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            count += len(left) - i  # All remaining left elements are inversions
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, count

# Test
nums = [3, 1, 2, 4]
print(f"List: {nums}")
print(f"Brute Force: {count_inversions_brute(nums)}")
_, optimal = count_inversions(nums)
print(f"Optimal: {optimal}")
