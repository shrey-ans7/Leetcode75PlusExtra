# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # if not root:
        #     return []
        # elif not root.left and not root.right:
        #     return [[root.val]] if root.val==targetSum else []
        res=[]
        def dfs(root,currSum,stack):
            nonlocal targetSum
            if not root:
                return
            stack.append(root.val)
            if currSum==targetSum-root.val and not root.left and not root.right:
                res.append(stack.copy())
                stack.pop()
                return

            dfs(root.left,currSum+root.val,stack)
            dfs(root.right,currSum+root.val,stack)

            stack.pop()
            return
        dfs(root,0,[])
        return res          
        
