class Solution:
    def countSubstrings(self, s: str) -> int:
        end = len(s) - 1
        if end < 0:
            return 0
        if end == 0:
            return 1

        count = 0
        dp = [[0 if i<j else -1 for i in range(end + 1)] for j in range(end + 1)]

        def dfs(i, j):
            nonlocal count
            if i < 0 or j > end:
                return 0
            if s[i] != s[j]:
                dp[i][j]=0
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 1 + dfs(i - 1, j + 1)
            count += 1
            return dp[i][j]

        for k in range(len(s)):
            # Check odd length palindromes
            dfs(k, k)
            # Check even length palindromes
            dfs(k, k + 1)
        # dp - count non zero entries
        return count
