class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return heights
        rows=len(heights)
        cols=len(heights[0])
        atlantic=set()
        pacific=set()
        def dfs(i,j,prev,visited):
            if i>=rows or j>=cols:
                return 
            if i<0 or j<0:
                return
            if (i,j) in visited:
                return 
            height=heights[i][j]
            if height>=prev:
                visited.add((i,j))
                dfs(i+1,j,height,visited)
                dfs(i,j+1,height,visited)
                dfs(i,j-1,height,visited)     
                dfs(i-1,j,height,visited)
            return 
        for i in range(rows):
            dfs(i,0,-sys.maxsize,pacific)     
        for j in range(cols):
            dfs(0,j,-sys.maxsize,pacific)   

        for i in range(rows):
            dfs(i,cols-1,-sys.maxsize,atlantic)     
        for j in range(cols):
            dfs(rows-1,j,-sys.maxsize,atlantic)   

        common=pacific.intersection(atlantic)
        return list(common)
