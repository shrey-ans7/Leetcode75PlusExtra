# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfsZigZag(root, takeRight, length):
            nonlocal res
            if not root:
                return length
            if takeRight:
                dfsZigZag(root.right,not takeRight, length+1)
                dfsZigZag(root.left, takeRight, 1)
            else:
                dfsZigZag(root.left,not takeRight, length+1)
                dfsZigZag(root.right, takeRight, 1)

            res=max(res,length)
            return length
        dfsZigZag(root, True, 0)
        return max(res,0)
        
            
        

            

            
            

