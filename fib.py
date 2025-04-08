class Solution:
    def fib(self, n: int) -> int:
        dp=[-1 for _ in range(n+1)]
        def dfs(i):
            if i==0:
                return 0
            elif i==1:
                return 1
            elif dp[i]!=-1:
                return dp[i]
            ans=dfs(i-1) + dfs(i-2)
            dp[i]=ans
            return ans
        return dfs(n)
        
