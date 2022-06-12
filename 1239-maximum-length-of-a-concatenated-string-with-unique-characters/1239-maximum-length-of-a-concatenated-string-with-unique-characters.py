class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        max_len = 0
        dict_arr = {}
        for i,item in enumerate(arr):
            dict_arr[i] = set(item)
            
        
        def dfs(i, res):
            if i >= len(arr):
                return res, len(res)
            
            if len(set(res)) != len(res):
                return '',0
            
            l = len(res)
            for j in range(i+1,len(arr)):
                if len(dict_arr[j].intersection(set(res))) == 0:
                    res,l = max(dfs(j, res + arr[j]), dfs(j,res),key=lambda x: x[1])
                    
            return res,l
        
        for i in range(len(arr)):
            res,l = dfs(i,arr[i])
            max_len = max(max_len,l)
        
        return max_len
                    
                
                
        