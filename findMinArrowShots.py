class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point:point[0])
        prev=points[0][1]
        size=len(points)
        count=1
        for i in range(1,size):
            if points[i][0]<=prev:
                prev=min(points[i][1],prev)
                continue
            else:
                count+=1
                prev=points[i][1]
        return count
        
