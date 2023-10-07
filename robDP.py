class Solution:
    dp={}    
    def helper(self, nums, i):
        high=len(nums)
        if high==0:
            return 0
        if i in self.dp.keys():
            return self.dp[i]
        ans1=nums[0]
        if high>2:
            ans1+=self.helper(nums[2:],i+2)
        ans2=self.helper(nums[1:],i+1)    
        self.dp[i] = max(ans1,ans2)
        return self.dp[i]
    def rob(self, nums: List[int]) -> int:
        self.dp={}
        return self.helper(nums, 0)
    
        
