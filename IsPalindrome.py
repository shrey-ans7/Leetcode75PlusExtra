class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        tuples = re.findall(r'[a-zA-Z0-9]',s)
        i=0
        j=len(tuples)-1
        print(tuples)
        while i<=j:
            if tuples[i].lower()!=tuples[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True
