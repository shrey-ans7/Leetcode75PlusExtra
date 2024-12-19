class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefix=[-1 for _ in range(n)]
        prefix[0]=height[0]
        suffix=[-1 for _ in range(n)]
        suffix[n-1]=height[n-1]
        total=0
        for i in range(1,n):
            prefix[i]=max(height[i],prefix[i-1])
            suffix[n-i-1]=max(height[n-i-1],suffix[n-i])
        print(suffix,prefix)
        for i in range(1,n-1):
            total+=max(0,min(prefix[i-1],suffix[i+1])-height[i])
        return total

        
