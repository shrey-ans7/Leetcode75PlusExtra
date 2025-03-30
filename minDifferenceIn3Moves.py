class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        end=len(nums)-1
        r=end
        curr=nums[r]-nums[l]
        i=0
        dp={}
        def dfs(l,r,i):
            if l==r:
                return 0
            if i==3:
                return nums[r]-nums[l]   
            if (l,r) in dp:
                return dp[(l,r)]  
            curr=nums[r]-nums[l]
            ans1 = dfs(l+1,r,i+1)
            ans2 = dfs(l,r-1,i+1)
            res=min(ans1,ans2,curr)
            dp[(l,r)]=res
            return res
        return dfs(l,r,0)
    
