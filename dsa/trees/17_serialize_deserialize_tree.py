# LeetCode 297 - Serialize and Deserialize Binary Tree
# Time: O(n) | Space: O(n)

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # Encodes a tree to a string.
    def serialize(self, root):
        if not root:
            return ""

        result = []
        q = deque([root])

        while q:
            node = q.popleft()

            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    # Decodes a string to a tree.
    def deserialize(self, data):
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        q = deque([root])

        i = 1
        while q:
            node = q.popleft()

            if values[i] != "null":
                node.left = TreeNode(int(values[i]))
                q.append(node.left)
            i += 1

            if values[i] != "null":
                node.right = TreeNode(int(values[i]))
                q.append(node.right)
            i += 1

        return root


# ---------- TEST ----------
# Tree:
#        1
#       / \
#      2   3
#         / \
#        4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()

data = codec.serialize(root)
print(data)

new_root = codec.deserialize(data)
print(codec.serialize(new_root))
