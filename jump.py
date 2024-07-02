
import sys
class Solution:
    def jump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        dp = [None for _ in range(goal)]
        def dfs(idx):
            if idx>=goal:
                return 0
            if dp[idx]!=None:
                return dp[idx]
            jump = sys.maxsize
            rang = nums[idx]
            if(rang==0):
                return jump
            for i in range(1,rang+1):
                jump = min(jump, dfs(idx+i))
            jump+=1
            dp[idx]=jump
            return jump
        return dfs(0)
            


        
