class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return None
        visitEdit=set()
        visit=set()
        visitNotEdit=set()
        m=len(board)
        n=len(board[0])
        queue=[]
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    queue.append((i,j))

        def dfs(node) -> bool:
            nonlocal visit, m, n
            i=node[0]; j=node[1] 
            if i<0 or j<0 or i>m-1 or j>n-1:
                return False
            elif board[i][j]=="X":
                return True
            elif node in visit:
                return True
            else:
                visit.add(node)
                return dfs((i+1,j)) and dfs((i-1,j)) and dfs((i,j+1)) and dfs((i,j-1))
        flag=False
        while queue:
            node = queue.pop()
            if node in visitEdit or node in visitNotEdit:
                continue
            flag=dfs(node)
            if flag:
                visitEdit.update(visit)
            else:
                visitNotEdit.update(visit)
            visit=set()
        
        for i in visitEdit:
            board[i[0]][i[1]]="X"
        return
