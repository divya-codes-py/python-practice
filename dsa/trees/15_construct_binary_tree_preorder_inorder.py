# LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal
# Preorder: [root, left subtree, right subtree]
# Inorder:  [left subtree, root, right subtree]
# Time: O(n) | Space: O(n)

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)  # split point

        root.left  = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],  inorder[mid+1:])
        return root

# ---------- TEST ----------
def inorder_list(node):
    if not node: return []
    return inorder_list(node.left) + [node.val] + inorder_list(node.right)

root = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
print(inorder_list(root))  # [9, 3, 15, 20, 7]
      
