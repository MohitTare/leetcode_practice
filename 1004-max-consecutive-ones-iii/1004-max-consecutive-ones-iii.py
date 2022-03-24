class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        max_count = 0
        r = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                if k == 0:
                    while(nums[l] != 0):
                        l+=1
                    l+=1
                else:
                    k-=1
            max_count = max(max_count,r - l + 1)
            
        return max_count
            
        