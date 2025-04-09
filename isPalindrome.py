class Solution:
    def isPalindrome(self, x: int) -> bool:
        orig=x
        rev=0
        while(orig>0):
            rev*=10
            rev+=(orig%10)
            orig=orig//10
        return rev==x
            
