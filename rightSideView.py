# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    map={}
    def helper(self, root, level):
        if not root:
            return
        self.map[level]=root.val
        self.helper(root.left, level+1)
        self.helper(root.right, level+1)
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.map={}
        self.helper(root, 0)
        ans=[]
        for i,j in self.map.items():
            ans.append([i,j])
        ans.sort(key=lambda x:x[0])
        for i in range(len(ans)):
            ans[i]=ans[i][1]
        return ans

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        return self.levelOrder(root)
        
        
