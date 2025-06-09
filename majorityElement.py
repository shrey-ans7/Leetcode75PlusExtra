class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr=nums[0]
        count=1
        for num in nums:
            if curr!=num:
                count-=1
            if count==0:
                curr=num
                count=1
            elif curr==num:
                count+=1
        return curr
            
        
