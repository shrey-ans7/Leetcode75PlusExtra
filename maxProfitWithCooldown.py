class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}
        size=len(prices)
        def dfs(i,isBuy):
            nonlocal size
            if i>=size:
                ans=-sys.maxsize
                if isBuy:
                    return 0
                return ans
            if (i,isBuy) in dp:
                return dp[(i,isBuy)]
            if isBuy:
                ans=-prices[i]
                ans+=dfs(i+1,not isBuy)
                ans=max(ans,dfs(i+1,isBuy))
            else:
                ans=prices[i]
                ans+=dfs(i+2,not isBuy)
                ans=max(ans,dfs(i+1,isBuy))
            dp[(i,isBuy)]=ans
            return ans
        return dfs(0,True)



        
