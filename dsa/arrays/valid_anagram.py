# Problem: Check if two strings are anagrams
# Interview Question: "Do both strings use the same letters same number of times?"
# LeetCode: #242

# Optimal Approach - Counter
# Time Complexity: O(n)
# Space Complexity: O(n)
from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

# Alternative - Sorting Approach
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def isAnagram_sort(s, t):
    return sorted(s) == sorted(t)

# Test
print(isAnagram("anagram", "nagaram"))   # True
print(isAnagram("rat", "car"))           # False
print(isAnagram("listen", "silent"))     # True
