class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def dfs(i,curr):
            if i >= len(nums) or sum(curr) > target:
                return 
            
            if sum(curr) == target:
                res.append(curr[:])
                return 
            
            for j in range(i, len(nums)):
                dfs(j,curr + [nums[j]])
            
        
        dfs(0,[])
        return res
                
            
            
        