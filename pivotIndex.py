class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        size=len(nums)
        prefix=[-1 for _ in range(size)]
        prefix[0]=nums[0]
        for i in range(1,size):
            prefix[i]=prefix[i-1]+nums[i]
        index=size
        for j in range(1,size):
            if prefix[j-1]==prefix[size-1]-prefix[j]:
                index=j
                break
        if prefix[size-1]-prefix[0]==0:
            return 0
        elif index!=size:
            return index
        elif prefix[size-2]==0:
            return size-1
        return -1
        
