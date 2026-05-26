# LeetCode #102 - Binary Tree Level Order Traversal
# Difficulty: Medium
# Time Complexity: O(n) - every node enqueued once
# Space Complexity: O(n) - queue holds at most one full level
# Interview: BFS template - reused in 10+ problems (right view, zigzag, avg)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_size = len(q)   # snapshot: nodes on this level
            level_vals = []

            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)

            result.append(level_vals)

        return result

# Test
root = TreeNode(3)
root.left  = TreeNode(9)
root.right = TreeNode(20)
root.right.left  = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
print("Level Order:", sol.levelOrder(root))
# Expected: [[3], [9, 20], [15, 7]]
