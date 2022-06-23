class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            target_sum = 0 - nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == target_sum:
                    if [nums[i],nums[l],nums[r]] not in res:
                        res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif curr_sum > target_sum:
                    r-=1
                elif curr_sum < target_sum:
                    l+=1
        
        return res
            
        