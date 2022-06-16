class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        
        def isPallindrome(s):
            return s == s[::-1]
        
        def dfs(s,path):
            if not s:
                res.append(path[:])
                return
                
            for i in range(1, len(s) + 1):
                if isPallindrome(s[:i]):
                    dfs(s[i:], path + [s[:i]])
                    
        dfs(s,[])
        return res
                
            
        