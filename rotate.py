#Better to solve using two pointers l,r -> swap(l,r).
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size=len(nums)
        k=k%size
        if size<=1:
            return nums
        if k>0:
            for i in range(size//2):
                nums[i],nums[size-1-i]=nums[size-1-i],nums[i]
            for i in range(k//2):
                nums[i],nums[k-1-i]=nums[k-1-i],nums[i]
            for i in range(size//2-k//2):
                nums[i+k],nums[size-1-i]=nums[size-1-i],nums[i+k]
        return nums
        
