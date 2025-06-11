class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows=len(matrix)
        cols=len(matrix[0])
        self.grid=[[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            self.grid[i][0]=matrix[i][0]
        for i in range(rows):
            for j in range(1,cols):
                self.grid[i][j]=matrix[i][j]+self.grid[i][j-1]
        

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res=0
        for i in range(row1, row2+1):
            res+=self.grid[i][col2]-(self.grid[i][col1-1] if col1>0 else 0)
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
