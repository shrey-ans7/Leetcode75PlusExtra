class Solution:
    def minOperations(self, nums: List[int]) -> int:
        size=len(nums)
        if size==1:
            return 0
        start=nums[0]
        for i in range(1,size):
            if nums[i]!=start:
                return 1
        return 0
        
        
