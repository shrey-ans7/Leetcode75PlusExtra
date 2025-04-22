class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        res=0
        prefixes={0:1}
        for num in nums:
            curr_sum+=num
            diff=curr_sum-k
            if diff in prefixes:
                res+=prefixes[diff]
            prefixes[curr_sum]=prefixes.get(curr_sum,0)+1
        return res
            

        
