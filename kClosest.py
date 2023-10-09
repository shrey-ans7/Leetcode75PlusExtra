class Point:
    def __init__(self,dist,cood):
        self.dist=dist
        self.cood=cood
    def __lt__(self,other):
        if self.dist<other.dist:
            return True
        return False
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists=[]
        heapq.heapify(dists)
        for i in points:
            dist=i[0]**2+i[1]**2
            heapq.heappush(dists,Point(-dist,i))
        while len(dists)>k:
            heapq.heappop(dists)
        res=[]
        for i in dists:
            res.append(i.cood)
        return res
        
