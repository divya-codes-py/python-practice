# LC 207 - Course Schedule
# Difficulty: Medium
# Pattern: Cycle Detection (DFS)
# Time: O(V+E) | Space: O(V+E)

class Solution:
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)

        # 0=unvisited, 1=visiting, 2=done
        state = [0] * numCourses

        def hasCycle(node):
            if state[node] == 1:  # Cycle sikt!
                return True
            if state[node] == 2:  # Safe node
                return False
            state[node] = 1
            for nei in graph[node]:
                if hasCycle(nei):
                    return True
            state[node] = 2
            return False

        return not any(hasCycle(i) for i in range(numCourses))
