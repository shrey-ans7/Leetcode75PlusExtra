class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        dup=-1
        miss=-1
        flag1=False
        flag2=False
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                dup=nums[i]
                flag1=True
            elif nums[i-1]!=nums[i]-1:
                miss=nums[i]-1
                flag2=True
            if flag1 and flag2:
                break
        if miss==-1:
            miss=1 if nums[0]!=1 else len(nums)
        return [dup,miss]
            

