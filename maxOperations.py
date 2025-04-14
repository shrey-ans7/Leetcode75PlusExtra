class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        nums.sort()
        size=len(nums)
        l=0;r=size-1
        while(l<r):
            addn=nums[l]+nums[r]
            if addn==k:
                count+=1
                l+=1
                r-=1
            elif addn<k:
                l+=1
            else:
                r-=1
        return count

