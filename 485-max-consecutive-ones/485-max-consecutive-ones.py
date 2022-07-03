class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        l = 0
        max_len = 0
        r = 0
        
        if len(nums) == 1:
            return nums[0]
        
        
        while r < len(nums):
            if nums[r] == 0:
                while r < len(nums) and nums[r] != 1:
                    r+=1
                if r >= len(nums):
                    return max_len
                else:
                    l = r
            max_len = max(max_len, r - l + 1)
            r+=1
        return max_len
            
    