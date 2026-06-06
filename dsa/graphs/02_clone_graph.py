# LeetCode 133 - Clone Graph
# Clone an undirected graph
# Time: O(V + E) | Space: O(V)

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]

            copy = Node(node.val)
            visited[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


# ---------- TEST ----------
# Graph:
#
#      1 ----- 2
#      |       |
#      |       |
#      4 ----- 3
#

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

clone = Solution().cloneGraph(node1)

print(clone.val)
print([n.val for n in clone.neighbors])

# Output:
# 1
# [2, 4]
