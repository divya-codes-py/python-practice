# LeetCode 236 - Lowest Common Ancestor of a Binary Tree
# Find the LCA of two nodes p and q in a binary tree
# Time: O(n) | Space: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: if root is None or root is one of the targets
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides returned a node → current root is the LCA
        if left and right:
            return root

        # Otherwise return whichever side found something
        return left if left else right


# ---------- TEST ----------
# Tree:      3
#          /   \
#         5     1
#        / \   / \
#       6   2 0   8
#          / \
#         7   4
# LCA(5, 1) = 3
# LCA(5, 4) = 5
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

sol = Solution()
print(sol.lowestCommonAncestor(root, root.left, root.right).val)       # 3
print(sol.lowestCommonAncestor(root, root.left, root.left.right.right).val)  # 5
