#Soln 1
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
#Soln 2       
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point:tuple(point))
        curr=points[0]
        count=1
        for point in points[1:]:
            if point[0]>curr[1]:
                count+=1
                curr=point
            else:
                curr[1]=min(curr[1],point[1])
        return count

        
