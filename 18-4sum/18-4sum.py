class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                curr_sum = target - (nums[i] + nums[j])
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < curr_sum:
                        l += 1
                    elif nums[l] + nums[r] == curr_sum:
                        if [nums[i], nums[j],nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j],nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > curr_sum:
                        r -= 1
        return res
                        
        