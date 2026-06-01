# Problem: Keep positives and negatives but group them separately
# Interview Question: "Separate negatives and positives while keeping order"

# Approach - Two Pass
# Time Complexity: O(n)
# Space Complexity: O(n)

def rearrange_pos_neg(numbers):
    negatives = []
    positives = []

    for num in numbers:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    return negatives + positives  # Negatives first, then positives

# Test
nums = [1, -2, 3, -4, 5, -6]
result = rearrange_pos_neg(nums)
print(f"Original: {nums}")
print(f"Rearranged: {result}")  # [-2, -4, -6, 1, 3, 5]
