import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap=[]
        self.maxHeap=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)
        if abs(len(self.minHeap)-len(self.maxHeap))<=1:
            if not self.minHeap:
                return
            if -self.maxHeap[0]<=self.minHeap[0]:
                return
            

        heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        while(-self.maxHeap[0]>self.minHeap[0]):
            heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        while(len(self.minHeap)-len(self.maxHeap)>1):
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
        return

    def findMedian(self) -> float:
        if len(self.minHeap)==len(self.maxHeap):
            return (self.minHeap[0]-self.maxHeap[0])/2
        else:
            if len(self.minHeap)<len(self.maxHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0] 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
