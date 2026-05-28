# LeetCode 572 - Subtree of Another Tree
# Check if tree 'sub' is a subtree of tree 'root'
# Time: O(m*n) | Space: O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)

# ---------- TEST ----------
root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub  = TreeNode(4, TreeNode(1), TreeNode(2))
print(Solution().isSubtree(root, sub))   # True

sub2 = TreeNode(4, TreeNode(1), TreeNode(3))
print(Solution().isSubtree(root, sub2))  # False
