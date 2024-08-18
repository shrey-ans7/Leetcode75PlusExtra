class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        size1 = len(word1)
        size2 = len(word2)
        dp = [[-1 for _ in range(size2)] for _ in range(size1)]
        def dfs(i,j):
            if i==size1: 
                return size2-j
            if j==size2:
                return size1-i
            if dp[i][j]!=-1:
                return dp[i][j]
            ans = sys.maxsize
            if word1[i]==word2[j]:
                ans = dfs(i+1,j+1)
                dp[i][j]=ans
                return ans

            ans = min(ans,1 + dfs(i,j+1))
            ans = min(ans,1 + dfs(i+1,j))
            ans = min(ans,1 + dfs(i+1,j+1))
            dp[i][j]=ans
            return ans
        return dfs(0,0)
        

            
