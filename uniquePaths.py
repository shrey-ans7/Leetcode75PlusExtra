#Soln 1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]+=dp[i-1][j]
                dp[i][j]+=dp[i][j-1]
        return dp[m-1][n-1]
#Soln 2:
class Solution:
    dp=None
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = [[-1 for _ in range(n)] for _ in range(m)]  
        self.dp[0][0]=1
        def helper(i, j):
            if i<0:
                return 0
            elif j<0:
                return 0
            elif i==0 and j==0:
                return 1
            elif self.dp[i][j]!=-1:
                return self.dp[i][j]
            
            ans1=helper(i,j-1)
            ans2=helper(i-1,j)

            self.dp[i][j]=ans1+ans2
            return self.dp[i][j]
        helper(m-1,n-1)
        return self.dp[m-1][n-1]
