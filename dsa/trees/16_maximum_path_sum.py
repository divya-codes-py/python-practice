# LeetCode 124 - Binary Tree Maximum Path Sum
# Find the maximum path sum in a binary tree
# Time: O(n) | Space: O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # Ignore negative paths
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # Path passing through current node
            current = node.val + left + right
            self.ans = max(self.ans, current)

            # Return one side to parent
            return node.val + max(left, right)

        dfs(root)
        return self.ans


# ---------- TEST ----------
# Tree:
#         -10
#         /  \
#        9   20
#           /  \
#          15   7
#
# Maximum Path = 15 + 20 + 7 = 42

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(Solution().maxPathSum(root))   # 42
