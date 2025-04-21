class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval:interval[0])
        size=len(intervals)
        count=0
        prev=intervals[0]
        for i in range(1,size):
            if intervals[i][0]<prev[1]:
                count+=1
                if intervals[i][1]<prev[1]:
                    prev=intervals[i]
            else:
                prev=intervals[i]
        return count

        
