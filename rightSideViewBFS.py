# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue1=deque()
        queue2=deque()
        level=0
        res=[]
        if not root:
            return res
        queue1.append(root)
        while (queue1):
            node = queue1.popleft()
            if len(res)<=level:
                res.append(node.val)
            else:
                res[level]=node.val
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
            if not queue1:
                while(queue2):
                    queue1.append(queue2.popleft())
                level+=1
        return res



        
