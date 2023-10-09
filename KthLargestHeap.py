import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums=nums
        self.k=k
        heapq.heapify(self.nums)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while len(self.nums)>self.k:
            heapq.heappop(self.nums)
        res=self.nums[0]
        return res


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
