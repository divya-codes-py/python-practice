# LeetCode #543 - Diameter of Binary Tree
# Difficulty: Easy
# Time Complexity: O(n) - single DFS pass
# Space Complexity: O(h) - recursion stack
# Interview: Same pattern as Max Path Sum - "return vs global update" insight

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def height(node):
            if not node:
                return 0
            L = height(node.left)
            R = height(node.right)
            # Diameter through this node = left height + right height
            self.diameter = max(self.diameter, L + R)
            # Return height to parent (only one direction)
            return 1 + max(L, R)

        height(root)
        return self.diameter

# Test
root = TreeNode(1)
root.left  = TreeNode(2)
root.right = TreeNode(3)
root.left.left  = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print("Diameter:", sol.diameterOfBinaryTree(root))  # Expected: 3
