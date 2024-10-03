class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        size=len(candies)
        flags=[False for _ in range(size)]
        maxCandies=max(candies)
        for i in range(size):
            if candies[i]+extraCandies>=maxCandies:
                flags[i]=True
        return flags
        
