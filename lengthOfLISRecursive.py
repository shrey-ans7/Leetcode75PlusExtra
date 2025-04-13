#1. Optimal Soln:
#TODO

#2. Accepted O(n^2) Memory and O(n^2) Time Soln:
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size=len(nums)
        dp=[[-1 for _ in range(size+1)] for _ in range(size+1)]
        nums.append(-sys.maxsize)
        def dfs(i,j):
            if i>=size:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            #1. Skip
            ans1=dfs(i+1,j)
            ans2=-1
            if nums[j]<nums[i]:
                ans2=1+dfs(i+1,i)
            ans2=max(ans1,ans2)
            dp[i][j]=ans2
            return ans2
            
        return dfs(0,size)
        
#3. Least Efficient Soln:
from typing import List, Dict
import sys

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}  # Memoization dictionary

        def dfs(index: int, prev_value: int) -> int:
            if index == n:
                return 0

            if (index, prev_value) in dp:
                return dp[(index, prev_value)]

            # Case 1: Skip the current element
            length = dfs(index + 1, prev_value)
            
            # Case 2: Include the current element if it's greater than the previous one
            if nums[index] > prev_value:
                length = max(length, 1 + dfs(index + 1, nums[index]))

            dp[(index, prev_value)] = length
            return length

        return dfs(0, -sys.maxsize)

