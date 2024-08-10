class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        n = len(word)
        rows = len(board)
        cols = len(board[0])
        # dp = [[[None for _ in range(cols)] for _ in range(rows)] for _ in range(n)]
        def dfs(i,j,count):
            if count==n:
                return True
            if i<0 or j<0 or i>=rows or j>=cols:
                return False
            if board[i][j]=="*":
                return False
            # if dp[count][i][j]!=None:
            #     return dp[count][i][j]
            temp = board[i][j]
            board[i][j] = "*"
            ans = False
            if temp==word[count]:
                ans = ans or dfs(i+1,j,count+1)
                ans = ans or dfs(i,j+1,count+1)
                ans = ans or dfs(i-1,j,count+1)
                ans = ans or dfs(i,j-1,count+1)
            # dp[count][i][j]=ans
            board[i][j]=temp
            return ans

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True
        return False
            
