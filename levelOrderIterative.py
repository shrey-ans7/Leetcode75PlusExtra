# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[root]
        res=[]
        while len(queue)!=0:
            ans=[]
            queue2=[]
            while len(queue)!=0:
                node=queue.pop(0)
                ans.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            res.append(ans)
            queue=queue2
        return res
        
        
