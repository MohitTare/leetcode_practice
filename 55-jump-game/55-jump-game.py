class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = r = 0
        
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
                print(i,farthest)
            
            if farthest == 0:
                return False
            
            l = r+1
            r = farthest
                
        if r >= len(nums) - 1: 
            return True
        