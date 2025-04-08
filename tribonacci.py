class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1 for _ in range(n+1)] 
        def dfs(i):
            if i==0:
                return 0
            elif i==1 or i==2:
                return 1
            elif dp[i]!=-1:
                return dp[i]
            ans=dfs(i-3)+dfs(i-2)+dfs(i-1)
            dp[i]=ans
            return ans
        return dfs(n)

        
