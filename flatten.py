#Soln 1:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev=None
        def dfs(root):
            nonlocal prev
            if not root:
                return
            dfs(root.right)
            dfs(root.left)
            root.right=prev
            root.left=None
            prev=root
            return 
        dfs(root)
        return root

#Soln 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        queue=[]
        def dfs(root):
            nonlocal queue
            if not root:
                return
            queue.append(root)
            dfs(root.left)
            dfs(root.right)
            return 
        dfs(root)
        queue[0].left=None
        for i in range(len(queue)-1):
            queue[i].right=queue[i+1]
            queue[i].left=None
        queue[len(queue)-1].right=None
        return queue[0]
            
        
