class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        self.res = 0
        dp = {}
        
        
        def dfs(i,target):
            if target < 0 or i >= len(nums):
                return 0
            
            if (i,target) in dp:
                return dp[(i,target)]
            
            if target == 0:
                dp[(i,target)] = 1
                return dp[(i,target)]
            
            dp[(i,target)] = 0
            for j in range(0,len(nums)):
                dp[(i,target)] = dp[(i,target)] + dfs(j, target - nums[j])
                
            return dp[(i,target)]
                
        
        return dfs(0,target)
                