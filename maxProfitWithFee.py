class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size=len(prices)
        dp=[[None for _ in range(2)] for _ in range(size)]
        buy=1
        def dfs(i, buy):
            ans = -sys.maxsize
            if i>=size:
                if buy:
                    return 0
                return ans
            if dp[i][buy]!=None:
                return dp[i][buy]
            if buy==1:
                ans=dfs(i+1,buy)
                ans=max(ans,dfs(i+1,buy-1)-prices[i]-fee)
            else:
                ans=dfs(i+1,buy)
                ans=max(ans,prices[i]+dfs(i+1,buy+1))
            dp[i][buy]=ans
            return ans
        return dfs(0,1)



        
