class Solution:
    def longestPalindrome(self, s: str) -> str:
        end = len(s) - 1
        if end < 0: 
            return ""
        if end == 0:  
            return s

        l = 0
        r = 1
        palLen = 1
        dp=[[-1 for _ in range(end+1)] for _ in range(end+1)]
        def dfs(i, j):
            if i < 0 or j > end or s[i] != s[j]:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            ans = 2 + dfs(i - 1, j + 1)
            dp[i][j] = ans
            return ans

        for k in range(len(s)):
            # Check odd length palindromes
            ans = 1 + dfs(k - 1, k + 1)
            if ans > palLen:
                palLen = ans
                mid = ans // 2
                l = k - mid
                r = k + mid + 1

            # Check even length palindromes
            ans = dfs(k-1, k)
            if ans > palLen:
                palLen = ans
                mid = ans // 2
                l = k - mid 
                r = k + mid 
                # dfs(k, k + 1)
                # l = k - mid + 1
                # r = k + mid + 1

        return s[l:r]
