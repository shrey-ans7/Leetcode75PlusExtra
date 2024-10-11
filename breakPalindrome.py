class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        size=len(palindrome)
        if size==1:
            return ""
        i=0
        palindrome=list(palindrome)
        while(i<size):
            if palindrome[i]!="a":
                if size%2==1 and i==size//2:
                    i+=1
                    continue
                palindrome[i]="a" 
                return "".join(palindrome)
            i+=1
        i=size-1
        while(i>=0):
            if palindrome[i]!="b":
                if size%2==1 and i==size//2:
                    i-=1
                    continue
                palindrome[i]="b" 
                return "".join(palindrome)
            i-=1
        return "".join(palindrome)
