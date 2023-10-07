# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        high=len(preorder)
        if high==0:
            return None
        root=TreeNode(preorder[0])
        for i in range(high):
            if preorder[0]==inorder[i]:
                break
        root.left=self.buildTree(preorder[1:i+1],inorder[:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])

        return root
        
