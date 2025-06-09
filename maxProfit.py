class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size=len(prices)
        start=-1
        res=0
        for i in range(0,size-1):
            if  start!=-1 and start<prices[i] and prices[i]<prices[i+1]:
                continue
            if start==-1 or start>prices[i]:
                start=prices[i]
            elif start<prices[i] and prices[i]>prices[i+1]:
                res+=prices[i]-start
                start=-1
        if start!=-1:
            res+=max(0,prices[size-1]-start)
        return res

        

