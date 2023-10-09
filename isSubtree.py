# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    flag=False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot==None and root==None:
            return True
        elif root==None:
            return False
        elif subRoot==None:
            return False
        flag1=False
        print(root.val, subRoot.val)
        if root.val==subRoot.val:
            if self.flag:
                return self.flag and self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
            else:
                self.flag=True
                flag1 = self.flag and self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
                self.flag=False
                if flag1:
                    return flag1
        if self.flag:
            return False
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
