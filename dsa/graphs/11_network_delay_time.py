# LeetCode 743 - Network Delay Time
# Find the minimum time required for all nodes to receive the signal.
# Time: O(E * log V) | Space: O(E)

from typing import List
import heapq


class Solution:
    def networkDelayTime(
        self,
        times: List[List[int]],
        n: int,
        k: int
    ) -> int:

        # Build adjacency list
        edges = {}

        for i in range(1, n + 1):
            edges[i] = []

        for src, dst, weight in times:
            edges[src].append((dst, weight))

        # Min Heap: (time, node)
        minHeap = [(0, k)]
        visited = set()
        maxTime = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited.add(node)
            maxTime = time

            for neighbor, weight in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(
                        minHeap,
                        (time + weight, neighbor)
                    )

        return maxTime if len(visited) == n else -1


# ---------- TEST ----------
times = [
    [2, 1, 1],
    [2, 3, 1],
    [3, 4, 1]
]

n = 4
k = 2

print(Solution().networkDelayTime(times, n, k))   # 2
