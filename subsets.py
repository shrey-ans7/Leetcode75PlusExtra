class Solution:
    def buildTree(self, nums):
        low=0
        high=len(nums)
        if high==0:
            return None
        val=nums.pop()
        root=TreeNode(val)
        mid=low+(high-low)//2
        root.left=self.buildTree(nums[mid:])
        root.right=self.buildTree(nums[0:high])
        return root

    def helper(self,root, stack, res):
        if not root:
            return
        
        stack.append(root.val) #Choose to take current element
        res.add(tuple(stack))
        self.helper(root.left, stack, res) #Take and goto left
        self.helper(root.right, stack, res) #Take and goto right
        stack.pop()

        res.add(tuple(stack)) #Choose to not take current element
        self.helper(root.left, stack, res) #Skip and goto left
        self.helper(root.right, stack, res) #Skip and goto right
        
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        root=self.buildTree(nums)
        res=set()
        if not root:
            return res
        stack=[]
        self.helper(root, stack, res)
        return res
