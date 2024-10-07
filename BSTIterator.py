# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[root]
        self.prev=-sys.maxsize

    def next(self) -> int:
        ptr=self.stack.pop()
        if ptr.left:
            if ptr.left.val>self.prev:
                self.stack.append(ptr)
                self.stack.append(ptr.left)
                return self.next()
            
            if ptr.right:
                self.stack.append(ptr.right)
            self.prev=ptr.val
            return self.prev
        else:
            self.prev=ptr.val
            if ptr.right:
                self.stack.append(ptr.right)
            return self.prev

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
