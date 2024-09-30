from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue=deque()
        nextFrontier=deque()
        queue.append(entrance)
        rows=len(maze)
        cols=len(maze[0])
        steps=0
        ops=[[0,1],[1,0],[0,-1],[-1,0]]
        visited=set()
        while queue:
            cood=queue.pop()
            if cood[0]==rows-1 or cood[0]==0:
                if cood!=entrance:
                    return steps
            elif cood[1]==cols-1 or cood[1]==0:
                if cood!=entrance:
                    return steps
            for op in ops:
                next=[rows,cols]
                next[0]=cood[0]+op[0]
                next[1]=cood[1]+op[1]
                
                if next[0]>=rows or next[0]<0:
                    continue
                elif next[1]>=cols or next[1]<0:
                    continue
                elif maze[next[0]][next[1]]=="+":
                    continue
                else:
                    nextStr=str(next)
                    if str(next) not in visited:
                        nextFrontier.append(next)
                        visited.add(nextStr)
            if not queue:
                steps+=1
                while nextFrontier:
                    queue.append(nextFrontier.popleft())
        return -1

            


        
