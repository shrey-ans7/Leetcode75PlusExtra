# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, total, targetSum):
        if not root:
            return False
        total+= root.val
        if total==targetSum:
            if not root.right and not root.left:
                return True

        part1 = self.helper(root.left, total, targetSum)
        part2 = self.helper(root.right, total, targetSum)
        return part1 or part2
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, 0, targetSum)
        
        
