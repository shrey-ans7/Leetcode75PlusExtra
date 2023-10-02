class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def trySpeed(piles, h, k, end):
            time=0
            for i in range(end):
                time+=math.ceil(float(piles[i]) / k)
            if time<=h:
                return True
            return False
        
        low=1
        high=max(piles)
        mid=low+(high-low)//2
        end=len(piles)
        res=-1
        while low<=high:
            mid=low+(high-low)//2
            if trySpeed(piles, h, mid, end):
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res

        
