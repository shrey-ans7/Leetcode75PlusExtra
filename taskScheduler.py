import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tracker={}
        for task in tasks:
            tracker[task]=tracker.get(task,0)+1
        heap=[]
        for task, freq in tracker.items():
            heapq.heappush(heap,-freq)
        q=deque()
        intervals=0
        while heap or q:
            intervals+=1
            while q and q[0][0]==intervals:
                _,freq=q.popleft()
                heapq.heappush(heap,freq)
            if heap:
                freq=heapq.heappop(heap)
                if freq+1<0:
                    q.append((intervals+n+1,freq+1))
            
        return intervals

        
        
