# LeetCode 199 - Binary Tree Right Side View
# Return the values visible from the right side (rightmost node per level)
# Time: O(n) | Space: O(n)

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                # Last node in the level = rightmost visible
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


# ---------- TEST ----------
# Tree:    1
#         / \
#        2   3
#         \   \
#          5   4
# Expected: [1, 3, 4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(Solution().rightSideView(root))  # [1, 3, 4]
