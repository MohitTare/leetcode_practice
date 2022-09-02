class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        
        def dfs(n_open,n_close,stack):
            if n_open == 0 and n_close==0:
               # print(stack)
                res.append(''.join(stack[:]))
                return
            
            if stack[-1] == '(':
                if n_open > 0:
                    dfs(n_open - 1,n_close, stack + ['('])
                if n_close > 0:
                    dfs(n_open,n_close - 1, stack + [')'])    
            else:
                if n_open > 0:
                    dfs(n_open - 1,n_close, stack + ['('])
                if n_close > n_open:
                    dfs(n_open,n_close - 1,stack + [')'])
                    
        dfs(n-1,n,['('])
        return res
                    
                
                
                    
                
                
                
                
                
                
            
            
        