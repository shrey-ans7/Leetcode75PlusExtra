from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited=set()
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        if not grid or not grid[0]:
            return -1
        elif grid[0][0]==1:
            return -1
        def expand(node):
            nonlocal queue, m, n, visited
            ops=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
            for op in ops:
                i=node[0]+op[0]
                j=node[1]+op[1]
                if i<0 or j <0 or i>m-1 or j>n-1:
                    continue
                elif (i,j) in visited or grid[i][j]==1:
                    continue
                visited.add((i,j))
                queue.append((i,j))
            return 
        queue.append((0,0))
        visited.add((0,0))
        length=0
        while queue:
            length+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                expand(node)
                if node[0]==m-1 and node[1]==n-1:
                    return length
        return -1




        
