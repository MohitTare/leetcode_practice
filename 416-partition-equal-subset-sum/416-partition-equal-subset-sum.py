class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
            
        target_sum = total_sum // 2
        
        dp = {}
        def dfs(i,target_sum):
            if i >= len(nums) or target_sum < 0:
                return False
            
            if (i,target_sum) in dp:
                return dp[(i,target_sum)]
            
            dp[(i,target_sum)] = False
            if target_sum == 0:
                dp[(i,target_sum)] = True
                return dp[(i,target_sum)] 
            
            dp[(i,target_sum)] =  dfs(i + 1, target_sum - nums[i]) or dfs(i + 1, target_sum)
            return dp[(i,target_sum)]
        
        return dfs(0,target_sum)
            
            