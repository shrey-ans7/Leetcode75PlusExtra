class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        dp = [None for _ in range(goal)]
        visited = set()
        def dfs(idx):
            if idx>=goal:
                return True
            if dp[idx]!=None:
                return dp[idx]
            flag=False
            if(nums[idx]==0):
                return False
            for i in range(1,nums[idx]+1):
                flag = flag or dfs(idx+i)
            dp[idx]=flag
            return flag
        return dfs(0)
            


        
