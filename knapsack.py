class Solution:
    def knapsack(self, W, val, wt):
        size=len(val)
        dp=[[-1 for _ in range(W+1)] for _ in range(size)]
        def dfs(i,w,):
            if i==size:
                return 0
            if dp[i][w]!=-1:
                return dp[i][w]
            ans1=dfs(i+1,w)
            if w-wt[i]>=0:
                ans1=max(ans1,val[i]+dfs(i+1,w-wt[i]))
            dp[i][w]=ans1
            return ans1
        return dfs(0,W)
      
class Solution:
    def knapsack(self, W, val, wt):
        size=len(val)
        dp=[[0 for _ in range(W+1)] for _ in range(size)]
      
        for j in range(wt[0],W+1):
            dp[0][j]=val[0];
          
        for i in range(1,size):
            for j in range(W+1):
                ans1=dp[i-1][j]
                take=-sys.maxsize
                if wt[i]<=j:
                    take=max(take,val[i]+dp[i-1][j-wt[i]])
                dp[i][j]=max(take,ans1)
              
        return dp[size-1][W]
