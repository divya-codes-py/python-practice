# LeetCode 1448 - Count Good Nodes in Binary Tree
# A node is "good" if no node on path from root to it has a greater value
# Time: O(n) | Space: O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, float('-inf'))

# ---------- TEST ----------
# Tree:   3
#        / \
#       1   4
#      /   / \
#     3   1   5
# Good nodes: 3, 4, 5, 3(left-left) → 4
root = TreeNode(3)
root.left = TreeNode(1, TreeNode(3), None)
root.right = TreeNode(4, TreeNode(1), TreeNode(5))
print(Solution().goodNodes(root))  # 4
