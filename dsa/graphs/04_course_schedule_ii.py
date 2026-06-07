# LeetCode 210 - Course Schedule II
# Return the order to finish all courses
# Time: O(V + E) | Space: O(V + E)

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            graph[course].append(pre)

        visiting = set()
        visited = set()
        order = []

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for pre in graph[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            visited.add(course)
            order.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order


# ---------- TEST ----------

print(Solution().findOrder(2, [[1, 0]]))
print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
