
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda intr:(intr[0],intr[1]))
        res=[intervals[0]]
        for intr in intervals[1:]:
            if res[-1][1]>=intr[0]:
                res[-1][0]=min(res[-1][0],intr[0])
                res[-1][1]=max(res[-1][1],intr[1])
            else:
                res.append(intr)
        return res
        
