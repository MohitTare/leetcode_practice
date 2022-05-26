class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)#base case
        
        target = sum(nums) // 2
        
        for i in range(len(nums) - 1, -1,-1):
            nextDp = set()
            for t in dp:
                nextDp.add(t + nums[i])
                nextDp.add(t)
            dp = nextDp
        
        return True if target in dp else False
        