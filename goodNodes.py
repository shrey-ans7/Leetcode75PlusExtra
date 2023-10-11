# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev=None
    def goodNodes(self, root: TreeNode) -> int:
        self.prev=-sys.maxsize
        count=0
        def dfs(root):
            nonlocal count
            if not root:
                return 
            temp=self.prev
            if root.val>=self.prev:
                count+=1
                self.prev=root.val
            dfs(root.left)
            self.prev=max(temp,root.val)
            dfs(root.right)
        dfs(root)
        return count
