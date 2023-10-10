from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        queue=deque()
        ops=[(0,1),(0,-1),(1,0),(-1,0)]
        def expand(node):
            nonlocal m, n, visited, ops, infected, count
            i=node[0]; j=node[1]
            t1=node[2]+1
            for op in ops:
                i1=i+op[0]; j1=j+op[1]
                if i1<0 or j1<0 or i1>m-1 or j1>n-1:
                    continue
                elif grid[i1][j1]!=1 or (i1,j1) in visited:
                    continue
                print(i1,j1)
                infected+=1
                queue.append((i1,j1,t1))
                visited.add((i1,j1))
                count = max(count,t1)
            return
        count=0
        fresh=0
        infected=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    infected+=1
                    queue.append((i,j,0))
                    visited.add((i,j))
        total=fresh+infected
        
        while(queue):
            node=queue.popleft()
            expand(node)
            if total==infected:
                return count
        print(infected, total)
        if total==infected:
            return count
        return -1



        
