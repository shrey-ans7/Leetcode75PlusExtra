#1. Greedy Solution
class Solution:
    def checkValidString(self, s: str) -> bool:
        size=len(s)
        charMap={}
        charMap["("]=1
        charMap[")"]=-1
        charMap["*"]=0
        leftMin=0
        leftMax=0
        for char in s:
            val=charMap[char]
            if val==0:
                leftMin-=1
                leftMin=max(leftMin,0)
                leftMax+=1
            else:
                leftMin+=val
                leftMin=max(leftMin,0)
                leftMax+=val
            if leftMax<0:
                return False
        if leftMin==0:
            return True
        return False

#2. DP Solution
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
        
