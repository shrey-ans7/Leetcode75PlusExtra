class Solution:
    dp=None
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        self.dp=[[-1 for _ in range(n)] for _ in range(m)]
        self.dp[0][0]==1
        def helper(i,j):
            if i<0 or j<0:
                return 0
            elif obstacleGrid[i][j]==1:
                return 0
            elif i==0 and j==0:
                return 1
            elif self.dp[i][j]!=-1:
                return self.dp[i][j]
            
            ans1=helper(i,j-1)
            ans2=helper(i-1,j)

            self.dp[i][j]=ans1+ans2
            return ans1+ans2
        return helper(m-1,n-1)
