# LeetCode 230 - Kth Smallest Element in a BST
# Inorder traversal of BST gives sorted order → return kth element
# Time: O(h + k) | Space: O(h)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative inorder - stops early at kth element
        stack = []
        curr = root
        count = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right

        return -1  # should never reach here with valid input

# ---------- TEST ----------
# BST:   3
#       / \
#      1   4
#       \
#        2
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(Solution().kthSmallest(root, 1))  # 1
print(Solution().kthSmallest(root, 3))  # 3
