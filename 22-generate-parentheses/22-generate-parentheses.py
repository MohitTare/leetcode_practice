class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(left,right,curr):
            if right < left :
                return
            if not left and not right:
                res.append(curr[:])
                return
            if left:
                dfs(left - 1,right, curr + '(')
            
            if right:
                dfs(left,right-1,curr + ')')
                
                
        dfs(n,n,'')
        return res
                
        
        