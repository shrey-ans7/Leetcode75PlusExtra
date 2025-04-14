class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0;r=0
        end=len(nums)
        count0s=0
        res=0
        zeroFlag=False
        while(l<=r and r<end):
            if nums[r]==0:
                zeroFlag=True
                count0s+=1
                while(count0s>1):
                    if nums[l]==0:
                        count0s-=1
                    l+=1
            res=max(res,r-l+1-count0s)
            r+=1
        if not zeroFlag:
            res-=1
        return res
