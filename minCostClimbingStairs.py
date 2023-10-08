class Solution:
    dp=None
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dp={}
        def dfs(i):
            if i>=len(cost):
                return 0
            if i in self.dp.keys():
                return self.dp[i]
            ans1=cost[i]
            ans1+=dfs(i+1)

            ans2=cost[i]
            ans2+=dfs(i+2)

            self.dp[i]=min(ans1, ans2)
            return self.dp[i]
        return min(dfs(0),dfs(1))
