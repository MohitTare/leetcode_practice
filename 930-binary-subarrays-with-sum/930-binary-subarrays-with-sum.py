class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    
        l = 0
        count = curr_sum = res = 0

        for r,num in enumerate(nums):
            curr_sum += nums[r]

            if num == 1:
                count = 0

            while l <= r and curr_sum >= goal:
                if curr_sum == goal:
                    count += 1

                curr_sum -= nums[l]
                l+=1

            res += count

        return res

    
                    
                
            
        

        
        
        
        