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

