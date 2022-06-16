class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        
        def dfs(i,curr):
            if i >= len(nums):
                if curr not in res:
                    res.append(curr[:])
                return
            
            if len(curr) > 0 and curr not in res:
                res.append(curr[:])
            
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            dfs(i+1,curr)
        
        dfs(0,[])
        return res