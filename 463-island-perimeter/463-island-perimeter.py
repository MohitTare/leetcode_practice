class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        
        
        def sum_adjacent(x,y):
            res = 0
            for dirx,diry in dirs:
                curr_x = x + dirx
                curr_y = y + diry
                if curr_x < 0 or curr_y < 0 or curr_x == R or curr_y == C or grid[curr_x][curr_y] == 0: # check for boundary cells and cells whose adjacent cell is water
                    res += 1
            return res
        
        perimeter = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    perimeter += sum_adjacent(r,c)
                    
        return perimeter
                    