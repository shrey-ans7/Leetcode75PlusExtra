# 1. Even more optimal soln
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size=len(nums)
        act=0
        for i in range(size):
            if nums[i]!=nums[act]:
                act+=1
                nums[act]=nums[i]
            
        return act+1
                
        

#2. Optimal Soln
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev=nums[0]-1
        size=len(nums)
        i=0
        count=0
        while i<size:
            if nums[i]==prev:
                i+=1
                continue
            else:
                nums[count]=nums[i]
                prev=nums[i]
                count+=1
                i+=1
        return count

#3. First Soln
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

        
