class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        total_sum = sum(nums)
        # Adjust range to account for negative values
        dp_range = 2 * total_sum + 1
        dp_offset = total_sum
        dp = [[None for _ in range(dp_range)] for _ in range(end + 1)]
        
        def dfs(i, currSum):
            if i > end:
                return 1 if currSum == target else 0
            if dp[i][currSum + dp_offset] is not None:
                return dp[i][currSum + dp_offset]
            ways = 0
            ans1 = nums[i] + currSum
            ways += dfs(i + 1, ans1)
            ans2 = -nums[i] + currSum
            ways += dfs(i + 1, ans2)
            dp[i][currSum + dp_offset] = ways
            return ways
        
        return dfs(0, 0)
