class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set("aeiou")
        count=0
        end=len(s)
        l=0; r=0
        res=0
        while(r-l<k):
            if s[r] in vowels:
                count+=1
            r+=1
        res=max(res,count)
        while(r<end):
            if s[l] in vowels:
                count-=1
            if s[r] in vowels:
                count+=1
            res=max(res,count)
            r+=1
            l+=1
        return res
            


        
