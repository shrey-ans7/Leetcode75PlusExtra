
#Soln 1:
class Solution:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    def reverse(self, x: int) -> int:
        is_neg=True if x<0 else False
        if is_neg:
            x*=-1
        seed=0
        while x:
            seed*=10
            seed+=x%10
            x=x//10
        if seed > self.INT_MAX or seed <self.INT_MIN:
            return 0
        return -seed if is_neg else seed
        
#Soln 2:

class Solution:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    def reverse(self, x: int) -> int:
        is_neg=True if x<0 else False
        if is_neg:
            x*=-1
        seed=(int(str(x)[::-1]))
        if seed > self.INT_MAX or seed <self.INT_MIN:
            return 0
        return -seed if is_neg else seed
        
