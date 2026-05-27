# LeetCode 112 - Path Sum
# Check if a root-to-leaf path exists with the given target sum
# Time: O(n) | Space: O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # At a leaf node: check if remaining equals leaf value
        if not root.left and not root.right:
            return root.val == targetSum

        remaining = targetSum - root.val
        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


# ---------- TEST ----------
# Tree:        5
#             / \
#            4   8
#           /   / \
#          11  13  4
#         /  \      \
#        7    2      1
# Target: 22 → path 5→4→11→2 = 22 ✓
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)

print(Solution().hasPathSum(root, 22))   # True
print(Solution().hasPathSum(root, 100))  # False
      
