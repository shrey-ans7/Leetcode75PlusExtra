#DP Solution
class Solution:
    def checkValidString(self, s: str) -> bool:
        size=len(s)
        dp={}
        def dfs(i,count):
            nonlocal size
            if count<0:
                return False
            if i>=size:
                if count==0:
                    return True
                else:
                    return False
            if (i,count) in dp:
                return dp[(i,count)]
            ans=False
            if s[i]=="(":
                ans = dfs(i+1,count+1)
            elif s[i]==")":
                ans = dfs(i+1,count-1)
            else:
                ans = dfs(i+1,count) or dfs(i+1,count+1) or dfs(i+1,count-1)
            dp[(i,count)]=ans
            return ans
        return dfs(0,0)
        
