class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        dict_count = defaultdict(lambda:0)
        l = 0
        max_one_len = 0
        for r in range(len(nums)):
            dict_count[nums[r]] += 1
            win_len = r - l + 1
            if dict_count[0] <= k:
                max_one_len = max(max_one_len,win_len)
            else:
                dict_count[nums[l]] -= 1
                l+=1
        
        return max_one_len
            
        