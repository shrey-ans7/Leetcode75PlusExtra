class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        dp = [[-1 for _ in range(size)] for _ in range(size)]
        def dfs(i,j):
            if i<0 or j<0 or i>=size or j>=size:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans=0        
            if s[i]==s[j]:
                ans=2
                if i==j:
                    ans=1
                ans += dfs(i-1,j+1)
            ans = max(ans, dfs(i,j+1))
            ans = max(ans, dfs(i-1,j))
            dp[i][j]=ans
            return ans
        res=0
        for i in range(size):
            res=max(res,dfs(i,i))
        return res
        

        
