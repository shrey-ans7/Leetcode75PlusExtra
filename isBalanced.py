# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        flag=True
        def dfs(root):
            nonlocal flag
            if not root:
                return 0
            ans=1
            ans1=dfs(root.left)
            ans2=dfs(root.right)
            if abs(ans1-ans2)>1:
                flag=False
            return max(ans1,ans2)+ans
        dfs(root)
        return flag
        
