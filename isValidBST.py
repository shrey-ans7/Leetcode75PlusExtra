# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev=None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.prev=-sys.maxsize
        
        def inorder(root):
            if not root:
                return True
            flag1=inorder(root.left)
            if root.val<=self.prev:
                return False
            self.prev=root.val
            return flag1 and inorder(root.right)
        return inorder(root)

                

         
        
