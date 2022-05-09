class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        dict_sum = defaultdict(lambda:0)
        dict_sum[0] = 1
        res = 0
        
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum - k in dict_sum:
                res += dict_sum[cum_sum - k]
            
            dict_sum[cum_sum] += 1
        return res
            
            
                
        