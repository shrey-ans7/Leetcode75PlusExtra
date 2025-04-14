class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0;r=0
        end=len(nums)
        count1s=0
        count0s=0
        res=0
        while(l<=r and r<end):
            if nums[r]==1:
                count1s+=1
                res=max(res,r-l+1)
            else:
                count0s+=1
                if count0s>k:
                    res=max(res,r-l)
                    while(count0s>k):
                        if nums[l]==0:
                            count0s-=1
                        l+=1
                else:
                    res=max(res,r-l+1)
            r+=1
        if count0s<k:
            res=max(res,r-l)
        return res
