class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        
        def gravityShift(grid):
            r = len(grid) - 1
            l = r - 1
        
            while l >= 0:
                if grid[l] == '#' and grid[r] == '.':
                    grid[r] = '#'
                    grid[l] = '.'
                    r-=1
                    l-=1
                elif grid[l] == '.' and grid[r] == '.':
                    l-=1
                elif grid[l] == '*':
                    l-=1
                    r = l
                else:
                    l-=1
                    r-=1
                    
        for grid in box:
            gravityShift(grid)
            
        return zip(*box[::-1]) 
                       
            
        
            
        
                    
        
                
        
                
        
        