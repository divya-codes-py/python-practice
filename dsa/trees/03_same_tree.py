# LeetCode #100 - Same Tree
# Difficulty: Easy
# Time Complexity: O(n) - n = min nodes in both trees
# Space Complexity: O(h) - recursion stack
# Interview: Tests clean recursive thinking with multiple base cases

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Both null -> same
        if not p and not q:
            return True
        # One null or values differ -> not same
        if not p or not q or p.val != q.val:
            return False
        # Recursively check left and right subtrees
        return (self.isSameTree(p.left,  q.left) and
                self.isSameTree(p.right, q.right))

# Test
p = TreeNode(1)
p.left  = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left  = TreeNode(2)
q.right = TreeNode(3)

sol = Solution()
print("Same Tree:", sol.isSameTree(p, q))   # Expected: True

q.right = TreeNode(5)
print("Same Tree:", sol.isSameTree(p, q))   # Expected: False
