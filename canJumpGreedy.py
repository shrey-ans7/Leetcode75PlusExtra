class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        maxIdx=0
        flag=False
        i=0
        while(maxIdx<goal and i<=maxIdx):
            rang = i + nums[i]
            maxIdx = max(maxIdx, rang)
            i+=1
        if maxIdx>=goal:
            flag=True
        return flag
        
            


        
