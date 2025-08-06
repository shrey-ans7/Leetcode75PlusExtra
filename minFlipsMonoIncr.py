class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp={}
        size=len(s)
        def dfs(i,mono):
            nonlocal size
            if i==size:
                return 0
            if (i,mono) in dp:
                return dp[(i,mono)]
            ans=size
            if s[i]=="1":
                if mono:
                    ans=min(1+dfs(i+1,mono),dfs(i+1,not mono))
                else:
                    ans=dfs(i+1,mono)
            else:
                if mono:
                    ans=dfs(i+1,mono)
                else:
                    ans=1+dfs(i+1, mono)
            dp[(i,mono)]=ans
            return ans
        return min(dfs(0,True),dfs(0,False))
        
