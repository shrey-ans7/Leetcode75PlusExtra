class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        size=1<<n
        grid=[[0 for _ in range(size)] for _ in range(size)]
        seed=0
        def solve(row,col,s):
            nonlocal grid,seed
            if s==1:
                grid[row][col]=seed
                seed+=1
                return
            s=s//2
            solve(row,col+s,s)
            solve(row+s,col+s,s)
            solve(row+s,col,s)
            solve(row,col,s)
            return
        solve(0,0,size)
        return grid

        
