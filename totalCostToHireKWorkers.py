class Worker:
    def __init__(self,cost,index):
        self.cost=cost
        self.index=index
    def __lt__(self,other):
        if self.cost<other.cost:
            return True
        elif self.cost==other.cost:
            return self.index<other.index
        return False
    
import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        costs=[Worker(cost,index) for index,cost in enumerate(costs)]
        heap=[]
        size=len(costs)
        for i in range(candidates):
            heapq.heappush(heap,costs[i])
        front_end=i
        back_end=max(front_end+1,size-candidates)
        for j in range(back_end,size):
            heapq.heappush(heap,costs[j])
        
        cost=0
        while k:
            worker=heapq.heappop(heap)
            k-=1
            cost+=worker.cost
            if front_end<back_end-1:
                if worker.index<=front_end:
                    front_end+=1
                    heapq.heappush(heap,costs[front_end])
                else:
                    back_end-=1
                    heapq.heappush(heap,costs[back_end])

        return cost


            
            

        
