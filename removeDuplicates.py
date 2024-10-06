from collections import deque
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newNums=deque()
        prev=nums[0]-1
        size=len(nums)
        count=0
        i=0
        while i<size-count:
            if nums[i]==prev:
                nums.pop(i)
                count+=1
            else:
                prev=nums[i]
                i+=1
        return size-count

        
