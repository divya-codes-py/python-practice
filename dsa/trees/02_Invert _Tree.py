# LeetCode #226 - Invert Binary Tree
# Difficulty: Easy
# Time Complexity: O(n) - visit every node once
# Space Complexity: O(h) - recursion stack
# Interview: Classic Google question - know recursive + iterative

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # Base case
        if not root:
            return None
        # Swap left and right children
        root.left, root.right = root.right, root.left
        # Recurse on both sides
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# --- Iterative BFS version ---
from collections import deque

def invertTree_BFS(root):
    if not root:
        return None
    q = deque([root])
    while q:
        node = q.popleft()
        node.left, node.right = node.right, node.left
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return root

# Helper to print tree level order
def levelOrder(root):
    if not root: return []
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    return res

# Test
root = TreeNode(4)
root.left  = TreeNode(2)
root.right = TreeNode(7)
root.left.left   = TreeNode(1)
root.left.right  = TreeNode(3)
root.right.left  = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()
inverted = sol.invertTree(root)
print("Inverted:", levelOrder(inverted))  # Expected: [4,7,2,9,6,3,1]
