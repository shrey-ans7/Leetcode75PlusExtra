#Soln 1:
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]

        # Start cell
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1

        # First column
        for i in range(1, m):
            if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1:
                dp[i][0] = 1

        # First row
        for j in range(1, n):
            if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1:
                dp[0][j] = 1

        # Fill rest of dp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
#Soln 2:
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
