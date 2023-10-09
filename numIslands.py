class Solution:
    dp=None
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j):
            nonlocal grid, visited
            if i<0 or j<0 or i>m-1 or j>n-1:
                return 
            elif grid[i][j]=="0" or (i,j) in visited:
                return 
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return
        count=0 
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visited:
                    dfs(i,j)
                    count+=1
        return count

        
        

        
