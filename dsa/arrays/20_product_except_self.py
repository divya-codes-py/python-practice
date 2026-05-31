# Problem: Product of Array Except Self
# Interview Question: "Return array where each element is product of all others"
# LeetCode: #238

# Optimal Approach - Prefix & Suffix Products
# Time Complexity: O(n)
# Space Complexity: O(1) - output array exclude maadidare

def product_except_self(numbers):
    n = len(numbers)
    result = [1] * n

    # Left pass - prefix products
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= numbers[i]

    # Right pass - suffix products
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= numbers[i]

    return result

# Test
nums = [1, 2, 3, 4]
result = product_except_self(nums)
print(f"List: {nums}")
print(f"Product except self: {result}")
