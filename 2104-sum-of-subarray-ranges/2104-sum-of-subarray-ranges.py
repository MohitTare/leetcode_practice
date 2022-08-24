class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min_el= float('inf')
        max_el = float('-inf')
        res = 0
        
        for i in range(len(nums)):
            min_el = nums[i]
            max_el = nums[i]
            for j in range(i,len(nums)):
                min_el = min(min_el,nums[i],nums[j])
                max_el = max(max_el,nums[i],nums[j])
                res += max_el-min_el
        
        return res