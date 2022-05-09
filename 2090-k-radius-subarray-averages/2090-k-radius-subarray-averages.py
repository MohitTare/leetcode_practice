class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        d = 2*k
        curr_sum = 0
        l = 0
        
        for r in range(len(nums)):
            curr_sum += nums[r]
            if l + r >= d:
                res[l+k] = curr_sum // (d + 1)
                curr_sum -= nums[l]
                l += 1
            
        return res
        