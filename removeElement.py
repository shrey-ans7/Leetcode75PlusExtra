class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[size]=nums[i]
                size+=1
        return size
        
