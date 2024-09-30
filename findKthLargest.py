#Explore Quickselect

#Solution 1
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums)>k:
            res=heapq.heappop(nums)
        return nums[0]
#Solution 2
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kNums=[]
        heapq.heapify(kNums)
        count=0
        for num in nums:
            if count==k:
                heapq.heappush(kNums,max(num,heapq.heappop(kNums)))
            else:
                heapq.heappush(kNums,num)
                count+=1
        return kNums[0]


        
