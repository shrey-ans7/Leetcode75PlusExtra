import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs=[(fir,sec) for fir,sec in zip(nums1,nums2)]
        pairs.sort(key=lambda pair:-pair[1])
        heap=[]
        i=0
        curr_sum=0
        size=len(pairs)
        while(i<k):
            curr_sum+=pairs[i][0]
            heapq.heappush(heap,pairs[i][0])
            i+=1
        res=curr_sum*pairs[k-1][1]
        while(i<size):
            curr_sum+=pairs[i][0]
            heapq.heappush(heap,pairs[i][0])
            evict=heapq.heappop(heap)
            curr_sum-=evict
            res=max(res,curr_sum*pairs[i][1])
            i+=1
        return res
