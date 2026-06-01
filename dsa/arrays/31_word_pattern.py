# Problem: Word Pattern
# Interview Question: "Does string s follow the same pattern?"
# LeetCode: #290

# Optimal Approach - Zip & Set
# Time Complexity: O(n)
# Space Complexity: O(n)

def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    # Unique pairs must equal unique chars in pattern and words
    return len(set(zip(pattern, words))) == len(set(pattern)) == len(set(words))

# Test
print(wordPattern("abba", "dog cat cat dog"))   # True
print(wordPattern("abba", "dog cat cat fish"))  # False
print(wordPattern("aaaa", "dog cat cat dog"))   # False
