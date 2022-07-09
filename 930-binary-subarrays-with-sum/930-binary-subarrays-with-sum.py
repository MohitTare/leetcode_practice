class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        res = 0
        count = 0
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            
            if nums[r] == 1:
                count = 0
                
            while l <= r and curr_sum >= goal:
                if curr_sum == goal:
                    count += 1
                
                curr_sum -= nums[l]
                l+=1
            res +=count
            
        return res
            
        

        
        
        
        