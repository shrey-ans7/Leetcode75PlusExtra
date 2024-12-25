class Solution:
    import math
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        size=len(nums)
        distincts=set()
        for index in range(size):
            current=nums[size-index-1]
            if current in distincts:
                break
            count+=1
            distincts.add(current)
        res=math.ceil((size-count)/3.0)
        return res
        
