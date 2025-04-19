class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        return (n&(n-1))==0
        
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while(n and n%2==0):
            n=n//2
        if n!=1:
            return False
        return True
        
            
        
