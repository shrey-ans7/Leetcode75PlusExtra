class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        part1 = [-1, -1, -1]
        fir=target[0]
        sec=target[1]
        thr=target[2]
        for i in triplets:
            if i[0]>fir or i[1]>sec or i[2]>thr:
                continue
            part1[0] = max(part1[0],i[0])
            part1[1] = max(part1[1],i[1])
            part1[2] = max(part1[2],i[2])
        if part1==target:
            return True
        return False
    
