# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. Using indices
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val_to_idx = {val:idx for idx,val in enumerate(inorder)}
        size=len(preorder)
        def dfs(preIndex, inStart, inEnd):
            if not inorder or not preorder:
                return None
            if inStart>inEnd:
                return None
            node=TreeNode(preorder[preIndex])
            mid=val_to_idx[preorder[preIndex]]
            node.left=dfs(preIndex+1,inStart,mid-1)
            node.right=dfs(preIndex+mid-inStart+1,mid+1,inEnd)
            return node
        return dfs(0,0,size-1)
# 2.Using Sub-lists
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
        
