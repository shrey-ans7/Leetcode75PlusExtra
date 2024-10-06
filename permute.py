class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size=len(nums)
        res=[]
        def dfs(i,nums,count,stack):
            nonlocal size
            stack.append(nums[i])
            value=nums.pop(i)
            for j in range(len(nums)):
                dfs(j,nums,count+1,stack)
            if count+1==size:
                res.append(stack.copy())
            stack.pop()
            nums.insert(i,value)
            return
        stack=[]
        for i in range(size):
            dfs(i,nums,0,stack)
        return res
            
            
            
        
