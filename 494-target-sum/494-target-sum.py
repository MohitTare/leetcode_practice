class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i,curr):
            if i == len(nums) and curr == target:
                dp[(i,curr)] = 1
            elif i == len(nums) and curr != target:
                dp[(i,curr)] = 0
                
            if (i,curr) not in dp:
                dp[(i,curr)] = dfs(i+1,curr + nums[i]) + dfs(i+1,curr - nums[i])
            
            return dp[(i,curr)]
        
        
        return dfs(0,0) 
            