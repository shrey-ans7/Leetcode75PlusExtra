class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        def dfs(i,j):
            nonlocal m, n, visited
            if i<0 or j<0 or i>m-1 or j>n-1:
                return 0
            if (i,j) in visited or grid[i][j]==0:
                return 0
            visited.add((i,j))
            ans=1
            ans+=dfs(i,j+1)
            ans+=dfs(i,j-1)
            ans+=dfs(i+1,j)
            ans+=dfs(i-1,j)
            return ans
        area=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and (i,j) not in visited:
                    area=max(dfs(i,j),area)
        return area

