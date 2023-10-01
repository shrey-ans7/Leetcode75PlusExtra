class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)
        mid = (low+high)//2
        print(nums, low, high, mid)
        if low==high:
            return -1
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            return self.search(nums[0:mid], target)
        else:
            tmp=self.search(nums[mid+1:high], target)
            if(tmp==-1):
                return -1
            return mid+1+tmp
