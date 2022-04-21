class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        seen = set()
        province = 0
        
        def dfs(i):
            for j,adj in enumerate(isConnected[i]):
                if adj == 1 and j not in seen:
                    seen.add(j)
                    dfs(j)
                    
        
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                province += 1
                
        return province
        