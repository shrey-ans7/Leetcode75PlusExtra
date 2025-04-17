class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        tracker={}
        n=len(grid)
        count=0
        for j in range(n):
            arr_str=""
            for i in range(n):
                arr_str+=str(grid[i][j])+","
            tracker[arr_str]=tracker.get(arr_str,0)+1
        for i in range(n):
            arr_str=""
            for j in range(n):
                arr_str+=str(grid[i][j])+","
            if arr_str in tracker:
                count+=tracker[arr_str]
        return count

        
