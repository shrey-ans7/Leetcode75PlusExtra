class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size=len(intervals)
        start=-1
        end=-1
        # size==0
        if size==0:
            return [newInterval]
        # start<0 and end<0
        if intervals[0][0]>newInterval[1]:
            return [newInterval]+intervals
        # start>=size and end>=size
        if intervals[size-1][1]<newInterval[0]:
            return intervals+[newInterval]
        startFlag=endFlag=True
        for i, interval in enumerate(intervals):
            if startFlag and interval[1]>=newInterval[0]:
                start=i
                startFlag=False
            if endFlag and interval[0]>newInterval[1]:
                end=i
                startFlag=False
                endFlag=False
            if not endFlag and not startFlag:
                break
        insertInterval=[-1,-1]
        if start>=0: # and intervals[start][0]>newInterval[0]:
            insertInterval[0]=min(newInterval[0],intervals[start][0])
        elif start<0:
            insertInterval[0]=newInterval[0]
            start=0
        if end>0 and end<size:
            insertInterval[1]=max(newInterval[1],intervals[end-1][1])
        elif end<0:
            end=size
            insertInterval[1]=max(newInterval[1],intervals[end-1][1])
        insertFlag=True
        ans=[]
        # start<0 but end<size
        # start>0 but end>=size
        # start>0 and end<size
        if start==end:
            intervals.insert(start,newInterval)
            return intervals
        for j in range(size):
            if j>=start and j<end:
                if insertFlag:
                    ans.append(insertInterval)
                    insertFlag=False
                continue
            ans.append(intervals[j])
        return ans
                

        


        
        
        

        
