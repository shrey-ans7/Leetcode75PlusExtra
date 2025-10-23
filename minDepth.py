# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root):
            if root and not root.left and not root.right:
                return 1
            if not root:
                return sys.maxsize
            left=1+dfs(root.left)
            right=1+dfs(root.right)
            return min(left,right)
        return dfs(root)
            
