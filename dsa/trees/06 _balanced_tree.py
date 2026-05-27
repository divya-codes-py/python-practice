# LeetCode 110 - Balanced Binary Tree
# Check if a binary tree is height-balanced (no subtree height diff > 1)
# Time: O(n) | Space: O(h) where h = height of tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            # Returns -1 if unbalanced, else returns height
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1


# ---------- TEST ----------
# Tree:     3
#          / \
#         9  20
#           /  \
#          15   7
# Expected: True
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(Solution().isBalanced(root))  # True

# Unbalanced tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)
root2.left.left.left = TreeNode(4)
print(Solution().isBalanced(root2))  # False
