class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        def dp_helper(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            
            dp[(r,c)] = 0
            
            down = dp_helper(r+1,c)
            right = dp_helper(r,c+1)
            diag = dp_helper(r+1,c+1)
            
            if matrix[r][c] == "1":
                dp[(r,c)] = 1 + min(down,right,diag)
            
            return dp[(r,c)]
        
        
            
        dp_helper(0,0)
        return max(dp.values()) ** 2
        
        
        