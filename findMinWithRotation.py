class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        index=low
        res=nums[0]
        while low<=high:
            mid=low+(high-low)//2
            res=min(nums[mid],res)
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid-1
        return res


        
