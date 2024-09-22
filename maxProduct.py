class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        dp = {}
        def dfs(i, currProd):
            if (i, currProd) in dp:
                return dp[(i,currProd)]
            ans=currProd
            if i+1<size:
                ans=max(ans,dfs(i+1,nums[i+1]))
                if currProd!=0:
                    ans=max(ans,dfs(i+1,currProd*nums[i+1]))
            dp[(i,currProd)]=ans
            return ans
        return dfs(0,nums[0])
        
