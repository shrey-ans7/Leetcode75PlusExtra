class Solution:
    def rob(self, nums: List[int]) -> int:
        end = len(nums)
        dp = [None for _ in range(end)]
        def dfs(i):
            nonlocal dp, end
            if i>=end:
                return 0
            elif dp[i]!=None:
                return dp[i]
            ans1 = dfs(i+1)
            ans2 = nums[i] + dfs(i+2)
            ans1 = max(ans1, ans2)
            dp[i]=ans1
            return ans1
        ans1 = dfs(1)
        dp = [None for _ in range(end)]
        end -= 1
        end = max(end,1)
        ans2 = dfs(0)
        return max(ans1,ans2)
        
