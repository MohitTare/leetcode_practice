class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i,curr,curr_sum):
            if len(curr) > k or curr_sum > n:
                return 
            
            if len(curr) == k and curr_sum == n:
                if curr not in res:
                    res.append(curr[:])
                return
            
            for j in range(i+1,11):
                dfs(j,curr + [i], curr_sum + i)
        
        
       
        for i in range(1,10):
            dfs(i,[],0)
        return res        