# LeetCode: 133. Clone Graph
# Topic: Graph, DFS
# Time Complexity: O(V + E)
# Space Complexity: O(V)

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        old_to_new = {}

        def dfs(curr):
            if curr in old_to_new:
                return old_to_new[curr]

            copy = Node(curr.val)
            old_to_new[curr] = copy

            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
