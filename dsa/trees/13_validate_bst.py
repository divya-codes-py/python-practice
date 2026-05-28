# LeetCode 98 - Validate Binary Search Tree
# BST rule: left < node < right (strictly), for ALL ancestors not just parent
# Time: O(n) | Space: O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float('-inf'), float('inf'))

# ---------- TEST ----------
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(Solution().isValidBST(root))   # True

root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(Solution().isValidBST(root2))  # False (4 < 5 but is right child)
