class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def dfs(ind):
            if ind < 0 or ind >= len(arr) or arr[ind] < 0:
                return False
            
            arr[ind] *= -1
            
            return arr[ind] == 0 or dfs(ind + arr[ind]) or dfs(ind - arr[ind])
        
        return dfs(start)
                
        
        

        