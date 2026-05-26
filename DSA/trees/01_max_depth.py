# LeetCode #104 - Maximum Depth of Binary Tree
# Difficulty: Easy
# Time Complexity: O(n) - visit every node once
# Space Complexity: O(h) - recursion stack, h = tree height
# Interview: Very common - know both recursive and iterative (BFS) versions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: empty node contributes 0 depth
        if not root:
            return 0
        # Recursively get depth of left and right subtree
        left_depth  = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # Current node adds 1 level to the deeper subtree
        return 1 + max(left_depth, right_depth)

# --- Iterative BFS version (also know this!) ---
from collections import deque

def maxDepth_BFS(root):
    if not root:
        return 0
    depth = 0
    q = deque([root])
    while q:
        depth += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
    return depth

# Test
root = TreeNode(3)
root.left  = TreeNode(9)
root.right = TreeNode(20)
root.right.left  = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print("Max Depth:", sol.maxDepth(root))   # Expected: 3
print("BFS Depth:", maxDepth_BFS(root))   # Expected: 3
      
