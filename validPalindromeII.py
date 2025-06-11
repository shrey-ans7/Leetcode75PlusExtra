class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        count=0
        flag=True
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            elif count==0:
                l+=1
                count+=1
            else:
                flag=False
                break
        if flag:
            return flag
        l=0
        r=len(s)-1
        count=0
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            elif count==0:
                r-=1
                count+=1
            else:
                return False
        return True



        
