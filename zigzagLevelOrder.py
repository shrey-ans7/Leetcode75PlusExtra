# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque()
        frontier=deque()
        res=[]
        queue.append(root)
        level=[]
        while queue:
            curr=queue.popleft()
            level.append(curr.val)
            if curr.left:
                frontier.append(curr.left)
            if curr.right:
                frontier.append(curr.right)
            if not queue:
                res.append(level)
                level=[]
                while frontier:
                    queue.append(
                        frontier.popleft())
        for i,level in enumerate(res):
            if i%2!=0:
                level.reverse()
        return res



        
