class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {'1':[],
                       '2':['a','b','c'],
                      '3':['d','e','f'],
                      '4':['g','h','i'],
                      '5': ['j','k','l'],
                      '6':['m','n','o'],
                      '7':['p','q','r','s'],
                       '8':['t','u','v'],
                       '9':['w','x','y','z'],
                       '*':['+'],
                       '0':[' ']
                        }
        if len(digits) == 0:
            return []
        
        res = []
        def dfs(s,curr):
            if not s and len(curr) == len(digits):
                res.append(''.join(curr[:]))
                return
            
            for i in range(len(s)):
                for l in letter_dict[s[i]]:
                    dfs(s[i+1:], curr + [l])
                    
        dfs(digits,[])
        return res