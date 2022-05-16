class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        low,end = 1, len(nums) - 1
        
        while(low + 1 <= end):
            mid = (low + end)//2
            count = 0
            for num in nums:
                if num <= mid: count += 1
            
            if count <= mid:
                low = mid + 1
            else:
                end = mid
                
        return end
        
        