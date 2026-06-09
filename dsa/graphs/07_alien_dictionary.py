# LeetCode Premium: 269. Alien Dictionary
# Topic: Graph, Topological Sort (Kahn's Algorithm)
# Time Complexity: O(C)
# Space Complexity: O(1) or O(C)
# C = Total number of characters in all words

from collections import deque


class Solution:
    def alienOrder(self, words):
        # Create graph with all unique characters
        graph = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in graph}

        # Build graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Invalid case
            if (
                len(word1) > len(word2)
                and word1.startswith(word2)
            ):
                return ""

            min_length = min(len(word1), len(word2))

            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        # Topological Sort
        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        order = []

        while queue:
            current = queue.popleft()
            order.append(current)

            for neighbor in graph[current]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detection
        if len(order) != len(graph):
            return ""

        return "".join(order)
