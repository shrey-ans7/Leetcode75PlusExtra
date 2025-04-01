"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        count=0
        starts=[interval.start for interval in intervals]
        ends=[interval.end for interval in intervals]
        starts.sort()
        ends.sort()
        end=len(intervals)
        l=0
        r=0
        res=0
        while (l<end and r<end):
            if starts[l]<ends[r]:
                count+=1
                l+=1
            elif ends[r]<=starts[l]:
                count-=1
                r+=1
            res=max(res,count)
        return res

                


    

        
