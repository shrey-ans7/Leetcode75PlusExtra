# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=0
        def dfs(root):
            if not root:
                return 0
            nonlocal res
            ans1=1
            ans2=dfs(root.left)
            ans3=dfs(root.right)
            res=max(res,ans2+ans3)
            return ans1+max(ans2,ans3)
        dfs(root)
        return res
        
        
        
