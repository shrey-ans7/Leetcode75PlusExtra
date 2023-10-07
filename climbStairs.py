class Solution:
    map={}
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        left=-1
        right=-1

        if n in self.map.keys():
            return self.map[n]

        if n-1 in self.map.keys():
            left=self.map[n-1]
        else: 
            left=self.climbStairs(n-1)
            self.map[n-1]=left

        if n-2 in self.map.keys():
            right=self.map[n-2]
        else: 
            right=self.climbStairs(n-2)
            self.map[n-2]=right
        self.map[n]=left+right
        return left+right
