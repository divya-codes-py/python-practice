# First Non-Repeating Character in Stream
# Time Complexity: O(n)
# Space Complexity: O(1) - bounded by alphabet size (26)

from collections import deque

def first_non_repeating(stream):
    queue = deque()
    freq = {}
    result = []

    for char in stream:
        freq[char] = freq.get(char, 0) + 1
        queue.append(char)

        while queue and freq[queue[0]] > 1:
            queue.popleft()

        result.append(queue[0] if queue else '#')

    return ''.join(result)


# Test
print(first_non_repeating("aabc"))   # a#bb -> wait, expected: a#bc? Let's check
# "a" -> a (only char)
# "aa" -> # (a repeated)
# "aab" -> b (a repeated, b is first non-repeat)
# "aabc" -> c? No: at "aabc", b and c both non-repeating, b came first -> b
# Output: a#bb  -- wait
# a -> 'a'
# aa -> '#'
# aab -> 'b'
# aabc -> 'b'  (b still first non-repeating)
# Correct output: "a#bb"
print(first_non_repeating("abcabc")) # a,a,a,#,#,#  -> "aaabbb"? 
# a->a, ab->a, abc->a, abca->b, abcab->c, abcabc-># 
# Correct output: "aaabc#"
