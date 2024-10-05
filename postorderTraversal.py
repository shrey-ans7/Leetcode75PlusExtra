# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        res=[]
        if root:
            stack.append(root)
        visited=set()
        while(stack):
            node=stack.pop()
            isLeaf=True
            buffer=[]
            if node.right and node.right not in visited:
                buffer.append(node.right)
                visited.add(node.right)
                isLeaf=False
            if node.left and node.left not in visited:
                buffer.append(node.left)
                visited.add(node.left)
                isLeaf=False
            if isLeaf:
                res.append(node.val)
            else:
                stack.append(node)
                for ptr in buffer:
                    stack.append(ptr)
        return res
            

        
