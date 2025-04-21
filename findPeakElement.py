class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        size=len(nums)
        l=0; r=size-1
        if r==0:
            return 0
        while(l<=r):
            mid=l+(r-l)//2
            if mid-1<0 and nums[mid+1]<nums[mid]:
                return mid
            elif mid+1>=size and nums[mid-1]<nums[mid]:
                return mid
            elif nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1
            

        
