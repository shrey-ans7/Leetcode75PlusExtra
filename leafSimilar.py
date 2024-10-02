# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf_seq1=[]
        leaf_seq2=[]
        size1=0
        size2=0
        def dfs(root, leaf_seq, size):
            if not root:
                return size
            size=dfs(root.left,leaf_seq,size)
            if not root.left and not root.right:
                size+=1
                leaf_seq.append(root.val)
                return size
            size=dfs(root.right,leaf_seq,size)
            return size
        size1=dfs(root1, leaf_seq1, size1)
        size2=dfs(root2, leaf_seq2, size2)
        if size1!=size2:
            return False
        else:
            for i in range(size1):
                if leaf_seq1[i]!=leaf_seq2[i]:
                    return False
        return True

                
