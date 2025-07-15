from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        
        # Prefix sums for top and bottom rows
        top = [0] * n
        bottom = [0] * n
        top[0] = grid[0][0]
        bottom[0] = grid[1][0]
        
        for i in range(1, n):
            top[i] = top[i-1] + grid[0][i]
            bottom[i] = bottom[i-1] + grid[1][i]
        
        result = float('inf')
        
        for i in range(n):
            # Top right sum: from i+1 to end
            top_right = top[-1] - top[i]
            # Bottom left sum: from 0 to i-1
            bottom_left = bottom[i-1] if i > 0 else 0
            
            second_player_score = max(top_right, bottom_left)
            result = min(result, second_player_score)
        
        return result
