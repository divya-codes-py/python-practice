# LC 133 - Clone Graph
# Difficulty: Medium
# Pattern: DFS + HashMap
# Time: O(V+E) | Space: O(V)

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]  # Already clone maadide
            clone = Node(node.val)
            visited[node] = clone    # Cycle handle maadak munche store
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)
