class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        end=len(coins)
        dp=[[-1 for _ in range(amount+1)] for _ in range(end+1)] 
        def dfs(i,amt):
            if amt==amount:
                return 0
            if amt>amount:
                return sys.maxsize
            if i==end:
                return sys.maxsize
            if dp[i][amt]!=-1:
                return dp[i][amt]
            ans1=dfs(i,amt+coins[i])
            ans1+=1
            ans1=min(ans1,dfs(i+1,amt))
            dp[i][amt]=ans1
            return ans1
        res=dfs(0,0)
        if res>amount:
            return -1
        return res
            
