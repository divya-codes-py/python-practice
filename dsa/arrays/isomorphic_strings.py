# Problem: Isomorphic Strings
# Interview Question: "Can characters of s be replaced to get t?"
# LeetCode: #205

# Optimal Approach - Zip & Set
# Time Complexity: O(n)
# Space Complexity: O(n)

def isIsomorphic(s, t):
    # Unique pairs must equal unique chars in both strings
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))

# Test
print(f"egg, add: {isIsomorphic('egg', 'add')}")     # True
print(f"foo, bar: {isIsomorphic('foo', 'bar')}")     # False
print(f"paper, title: {isIsomorphic('paper', 'title')}")  # True
