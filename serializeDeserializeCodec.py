from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        if not root:
            return ""
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("#")
        # remove trailing '#'
        while res and res[-1] == "#":
            res.pop()
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q and i < len(vals):
            node = q.popleft()

            # left child
            if i < len(vals) and vals[i] != "#":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1

            # right child
            if i < len(vals) and vals[i] != "#":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1

        return root
