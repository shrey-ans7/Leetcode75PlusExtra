# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=-sys.maxsize
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            ans=root.val
            res=max(res,ans)
            left=dfs(root.left)
            right=dfs(root.right)
            max_branch=max(left,right,0)
            res=max(res,ans+max_branch,left+ans+right)
            return ans+max_branch
        dfs(root)
        return res
        
