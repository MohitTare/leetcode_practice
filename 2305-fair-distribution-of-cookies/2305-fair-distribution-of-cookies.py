class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        
        self.res = float('inf')
        
        def dfs(i):
            if i  == len(cookies):
                self.res = min(self.res,max(children))
                return
            
            
            if self.res <= max(cookies):
                return
            
            for child in range(k):
                #print(f"before call {children,self.res}")
                children[child] += cookies[i]
                dfs(i+1)
                children[child] -= cookies[i]
                #print(f"After call {children,self.res}")
                
        dfs(0)
        return self.res
            
        
        
        
        
            
        
        
        
        