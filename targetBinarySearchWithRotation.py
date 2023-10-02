class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        if high<0:
            return -1
        res=nums[0]
        pivot=0
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]<res:
                res=nums[mid]
                pivot=mid
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid-1
        def helper(nums, target):
            low=0
            high=len(nums)-1
            while low<=high:
                mid=low+(high-low)//2
                print(nums[mid])
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        index=helper(nums[0:pivot],target)
        if index==-1:
            high=len(nums)
            index=helper(nums[pivot:high],target)
            if index==-1:
                return index
            return pivot+index
        else:
            return index

        
