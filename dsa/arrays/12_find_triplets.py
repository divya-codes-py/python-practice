# Problem: Find all triplets that add up to zero
# Interview Question: "Find three numbers from the list that sum to 0"
# LeetCode: #15

# Optimal Approach - Sort + Two Pointer
# Time Complexity: O(n²)
# Space Complexity: O(n)

def find_triplets(numbers):
    numbers.sort()
    triplets = []

    for i in range(len(numbers) - 2):
        left = i + 1
        right = len(numbers) - 1

        while left < right:
            total = numbers[i] + numbers[left] + numbers[right]

            if total == 0:
                triplet = [numbers[i], numbers[left], numbers[right]]
                if triplet not in triplets:
                    triplets.append(triplet)
                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Need bigger sum
            else:
                right -= 1  # Need smaller sum

    return triplets

# Test
nums = [-1, 0, 1, 2, -1, -4]
print(f"List: {nums}")
print(f"Triplets: {find_triplets(nums)}")  # [[-1,-1,2], [-1,0,1]]
