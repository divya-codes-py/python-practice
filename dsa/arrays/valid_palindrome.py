# Problem: Valid Palindrome
# Interview Question: "Check if string is palindrome ignoring spaces and special chars"
# LeetCode: #125

# Optimal Approach - Two Pointer
# Time Complexity: O(n)
# Space Complexity: O(n)

def isPalindrome(s):
    # Keep only alphanumeric characters, convert to lowercase
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

# Test
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
print(isPalindrome("race a car"))                       # False
print(isPalindrome("Was it a car or a cat I saw?"))    # True
