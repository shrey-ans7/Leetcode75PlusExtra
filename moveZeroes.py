class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        size=len(nums)
        while i<size:
            if nums[size-i-1]==0:
                j=size-i-1
                while j+1<size:
                    if nums[j+1]!=0:
                        swap=nums[j+1]
                        nums[j+1]=nums[j]
                        nums[j]=swap
                        j+=1
                    else:
                        break
            i+=1
