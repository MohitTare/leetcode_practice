class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        ans = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                while(nums[l] != 0):
                    l+=1
                l+=1
            ans = max(ans,r-l+1)
            
        return ans