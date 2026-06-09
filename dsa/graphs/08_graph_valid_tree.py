# LeetCode Premium: 261. Graph Valid Tree
# Topic: Graph, DFS
# Time Complexity: O(V + E)
# Space Complexity: O(V)

from collections import defaultdict


class Solution:
    def validTree(self, n, edges):
        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        graph = defaultdict(list)

        # Build undirected graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        # Check for cycle
        if not dfs(0, -1):
            return False

        # Check graph is connected
        return len(visited) == n
