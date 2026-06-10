# LeetCode 547 - Number of Provinces
# Count the number of connected components (provinces)
# in an undirected graph represented as an adjacency matrix.
# Time: O(n * n) | Space: O(n)

from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0

        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for neighbor in range(n):
                if (
                    isConnected[city][neighbor] == 1
                    and neighbor not in visited
                ):
                    visited.add(neighbor)
                    dfs(neighbor)

        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1

        return provinces


# ---------- TEST ----------
isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

print(Solution().findCircleNum(isConnected))   # 2
