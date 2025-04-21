#O(n) Time and O(1) Space
class Solution:
    MOD = 10**9 + 7

    def numTilings(self, n: int) -> int:
        # f(i) = # of ways to fully tile 2×i
        # g(i) = # of ways to tile 2×i with a “hanging” cell at column i
        full_1, full_2 = 1, 1    # f(1)=1, f(0)=1
        top_m, bottom_m = 0, 0   # g(1)=0, g(1)=0

        for _ in range(2, n+1):
            new_full   = (full_1 + full_2 + top_m + bottom_m) % self.MOD
            new_top    = (bottom_m + full_2) % self.MOD
            new_bottom = (top_m    + full_2) % self.MOD

            full_2, full_1 = full_1, new_full
            top_m, bottom_m = new_top, new_bottom

        return full_1
#O(n) Space and Time
class Solution:
    mod=10**9+7
    def numTilings(self, n: int) -> int:
        full, top_m, bottom_m = {0:1,1:1},{1:0},{1:0}
        for i in range(2,n+1):
            full[i]=full[i-1]+full[i-2]+top_m[i-1]+bottom_m[i-1]
            top_m[i]=top_m[i-1]+full[i-2]
            bottom_m[i]=bottom_m[i-1]+full[i-2]
        return full[n]%self.mod
        
