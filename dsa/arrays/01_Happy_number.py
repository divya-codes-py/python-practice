# Problem: Happy Number
# Interview Question: "Is a number happy? Sum of squares of digits eventually reaches 1"
# LeetCode: #202

# Approach - HashSet to detect cycle
# Time Complexity: O(log n)
# Space Complexity: O(log n)

def isHappy(n):
    seen = set()
    while n != 1:
        n = sum(int(d) ** 2 for d in str(n))  # Sum of squares of digits
        if n in seen:
            return False  # Cycle detected — not happy
        seen.add(n)
    return True

# Test
print(f"19 is happy: {isHappy(19)}")   # True
print(f"2 is happy: {isHappy(2)}")     # False
print(f"7 is happy: {isHappy(7)}")     # True
