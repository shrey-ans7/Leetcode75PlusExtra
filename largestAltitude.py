class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        size=len(gain)
        prefix=gain[0]
        res=max(gain[0],0)
        for i in range(1,size):
            prefix=gain[i]+prefix
            res=max(res,prefix)
        return res
        

# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         size=len(gain)
#         prefix = [-1 for _ in range(size)]
#         prefix[0]=gain[0]
#         res=max(gain[0],0)
#         for i in range(1,size):
#             prefix[i]=gain[i]+prefix[i-1]
#             res=max(res,prefix[i])
#         return res
        
