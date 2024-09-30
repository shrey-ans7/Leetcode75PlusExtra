# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque()
        queue.append(root)
        res=root.val
        nextFrontier=deque()
        ans=0
        level=0
        resLevel=1
        while queue:
            node=queue.popleft()
            ans+=node.val
            if node.left:
                nextFrontier.append(node.left)
            if node.right:
                nextFrontier.append(node.right)
            if not queue:
                level+=1
                if ans>res:
                    res=ans
                    resLevel=level
                ans=0
                while nextFrontier:
                    queue.append(nextFrontier.popleft())

        return resLevel

        
