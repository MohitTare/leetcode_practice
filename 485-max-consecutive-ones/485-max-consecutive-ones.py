class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        l = 0
        max_len = 0
        r = 0
        
        if len(nums) == 1:
            return nums[0]
        
        
        for r in range(len(nums)):
            if nums[r] == 0:
                while nums[l] != 0:
                    l+=1
                l+=1
            max_len = max(max_len, r - l + 1)
        return max_len
            
    