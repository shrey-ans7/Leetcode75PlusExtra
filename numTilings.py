class Solution:
    mod=10**9+7
    def numTilings(self, n: int) -> int:
        full, top_m, bottom_m = {0:1,1:1},{1:0},{1:0}
        for i in range(2,n+1):
            full[i]=full[i-1]+full[i-2]+top_m[i-1]+bottom_m[i-1]
            top_m[i]=top_m[i-1]+full[i-2]
            bottom_m[i]=bottom_m[i-1]+full[i-2]
        return full[n]%self.mod
        
