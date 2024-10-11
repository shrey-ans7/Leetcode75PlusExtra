class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        size1=len(s)
        size2=len(t)
        dp=[[-1 for _ in range(size2)] for _ in range(size1)]
        def dfs(i,j):
            nonlocal size1,size2
            if j>=size2:
                return 1
            if i>=size1:
                return 0
            ans=dp[i][j]
            if ans!=-1:
                return ans
            ans=0
            if s[i]==t[j]:
                ans+=dfs(i+1,j+1)
            ans+=dfs(i+1,j)
            dp[i][j]=ans
            return ans
        return dfs(0,0)

        
