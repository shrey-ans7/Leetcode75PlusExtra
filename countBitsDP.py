class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0 for _ in range(n+1)]
        dp[0]=0
        offset=1
        for num in range(1,n+1):
            if num==2*offset:
                offset=num
            dp[num]=1+dp[num-offset]
            
        return dp
