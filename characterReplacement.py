class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        l=0
        r=1
        end=len(s)
        counts={}
        counts[s[0]]=1
        while (l<r and r<end):
            counts[s[r]]=counts.get(s[r],0)+1
            while(r-l+1-max(counts.values())>k):
                counts[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
            r+=1
        return res

