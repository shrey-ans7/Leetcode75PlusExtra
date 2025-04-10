class Solution:
    def mySqrt(self, x: int) -> int:
        high=x
        low=0
        while(low<=high):
            mid=low+(high-low)//2
            squaredMid=mid**2
            if squaredMid==x:
                return mid
            elif squaredMid<x:
                low=mid+1
            else:
                high=mid-1
        return high

        
