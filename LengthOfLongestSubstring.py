class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strs=list(s)
        end=len(s)
        i=0; j=1 
        covered={}
        if(end==0):
            return 0
        covered[strs[i]]=i
        ans=j-i
        res=j-i
        while j<end:
            if strs[j] in covered.keys():
                i=max(covered[strs[j]]+1,i)
                covered[strs[j]]=j
                ans=j-i+1
                res=max(res,ans)
            else:
                ans=j-i+1
                covered[strs[j]]=j
                res=max(res,ans)
            j+=1
        return res
