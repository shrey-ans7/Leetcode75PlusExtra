import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            s1=abs(heapq.heappop(stones))
            s2=abs(heapq.heappop(stones))
            if s1==s2:
                continue
            else:
                s1-=s2
                heapq.heappush(stones,-s1)
        if len(stones)==1:
            return abs(stones[0])
        return 0
