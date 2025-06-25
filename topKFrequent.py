class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker={}
        for num in nums:
            tracker[num]=tracker.get(num,0)+1
        import heapq
        queue=[]
        for key, value in tracker.items():
            heapq.heappush(queue,(value, key))
            if len(queue)>k:
                heapq.heappop(queue)
        return [key for val, key in queue]


        
