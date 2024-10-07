#1. Optimal Solution with 2D DP:
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        size=len(nums)
        dp = [[-1 for _ in range(size+2)] for _ in range(size+2)]
        nums.insert(0,1)
        nums.append(1)
        def dfs(i,j):
            if j-i==1:
                return nums[i-1]*nums[i]*nums[j]
            if i==j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=-sys.maxsize
            for k in range(i,j):
                coins=dfs(i,k)+dfs(k+1,j)+nums[i-1]*nums[k]*nums[j]
                dp[i][j]=max(dp[i][j],coins)
            return dp[i][j]
        return dfs(1,size+1)

#2. Original experimental n! draft with a version of DP:
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        size = len(nums)
        dp = {}
        def dfs(i,nums):
            nums_str = str(nums)
            if (i,nums_str) in dp:
                return dp[(i,nums_str)]

            if i>len(nums):
                return 0
            res=1
            for j in range(max(0,i-1),min(i+2,len(nums))):
                res*=nums[j]
            value=nums.pop(i)
            next=0
            for k in range(len(nums)):
                next=max(next,dfs(k,nums))
            nums.insert(i,value)
            dp[(i,nums_str)]=res+next
            return res+next
        res=0
        for i in range(len(nums)):
            res=max(res,dfs(i,nums))
        return res     
