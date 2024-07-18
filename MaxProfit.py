class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minPrice=prices[0]
        for price in prices:
            minPrice=min(price,minPrice)
            profit=max(profit,price-minPrice)
        return profit

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l=len(prices)
#         import sys
#         prefix = [sys.maxsize]*l
#         suffix = [-1]*l
#         prefix[0]=prices[0]
#         for i in range(1,l):
#             prefix[i]=min(prefix[i-1],prices[i])
#         suffix[l-1]=prices[l-1]
#         for i in range(l-2,-1,-1):
#             suffix[i]=max(suffix[i+1],prices[i])
#         ans=0
#         for i in range(0,l):
#             temp=suffix[i]-prefix[i]
#             if ans<temp:
#                 ans=temp
#         return ans
            
