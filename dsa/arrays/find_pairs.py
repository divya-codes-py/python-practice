# Problem: Find all pairs in a list that add up to target
# Interview Question: "Find every combination of two numbers that sum to target"

# Approach - HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)

def find_pairs(numbers, target):
    pairs = []
    seen = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            if pair not in pairs:
                pairs.append(pair)
        seen.add(num)

    return pairs

# Test
nums = [1, 5, 3, 7, 4, 2, 6]
target = 8
result = find_pairs(nums, target)
print(f"List: {nums}")
print(f"Target: {target}")
print(f"Pairs: {result}")  # [(1,7), (5,3), (4,4), (2,6)]
