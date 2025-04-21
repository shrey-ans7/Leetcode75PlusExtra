class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        res=0
        def dfs(i,j):
            nonlocal res
            if i>=m or j>=n:
                return 0
            elif dp[i][j]!=-1:
                return dp[i][j]
            ans=1 if matrix[i][j]=="1" else 0
            ans+=min(dfs(i+1,j),dfs(i+1,j+1),dfs(i,j+1))*ans
            dp[i][j]=ans
            res=max(res,ans)
            return ans
        dfs(0,0)
        return res**2


        
