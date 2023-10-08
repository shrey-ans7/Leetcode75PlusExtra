class Solution:
    dp=None
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        self.dp=[[-1 for _ in range(n)] for _ in range(m)]
        def helper(i,j):
            if i<0 or j<0:
                return 0
            elif i>=m or j>=n:
                return 0
            elif self.dp[i][j]!=-1:
                return self.dp[i][j]
            ans1=0
            if text1[i]==text2[j]:
                ans1=1+helper(i+1,j+1)
            ans2=helper(i+1,j)
            ans3=helper(i,j+1)
            res=max(ans1,ans2,ans3)
            self.dp[i][j]=res
            return res
        return helper(0,0)
                
