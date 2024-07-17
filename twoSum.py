class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2=[]
        for i in range(len(nums)):
            nums2.append([nums[i],i])
        nums2.sort( key = lambda x:x[0])
        i=0; j=len(nums)-1
        while i<j:
            if nums2[i][0]+nums2[j][0]<target:
                i+=1
            elif nums2[i][0]+nums2[j][0]>target:
                j-=1
            else:
                i=nums2[i][1]
                j=nums2[j][1]
                break
        res=[i,j]
        res.sort()
        return res
        
