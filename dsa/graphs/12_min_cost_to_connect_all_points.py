# LeetCode 1584 - Min Cost to Connect All Points
# Find the minimum cost to connect all points.
# Time: O(n² log n) | Space: O(n²)

from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Build adjacency list
        adj = {i: [] for i in range(n)}

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append((dist, j))
                adj[j].append((dist, i))

        cost = 0
        visited = set()
        minHeap = [(0, 0)]  # (cost, node)

        while len(visited) < n:
            weight, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            cost += weight

            for nextWeight, neighbor in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        minHeap,
                        (nextWeight, neighbor)
                    )

        return cost


# ---------- TEST ----------
points = [
    [0, 0],
    [2, 2],
    [3, 10],
    [5, 2],
    [7, 0]
]

print(Solution().minCostConnectPoints(points))   # 20
