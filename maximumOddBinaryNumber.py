class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        size=len(s)
        s=list(s)
        onesCount=0
        for char in s:
            if char=="1":
                onesCount+=1
            
        if s[size-1]!="1":
            s[size-1]="1"
        onesCount-=1
        for i in range(0,size-1):
            if i<onesCount:
                s[i]="1"
            else:
                s[i]="0"
        return "".join(s)
        
