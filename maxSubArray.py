class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxLen = len(nums)
        L=0; R=L
        maxL=L; maxR=R
        res = nums[L]
        tot = 0
        while R<maxLen:
            tot+=nums[R]
            if tot>res:
                res=tot
                maxL=L
                L=R
                maxR=R

            if tot<0:
                tot=0
                R+=1
                continue
            R+=1
        #maxR+=1
        return res
