class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        lowerDiff = {}
        higherDiff = {}
        
        result = set()
        
        for num in nums:
            if num in lowerDiff:
                result.add((num,lowerDiff[num]))
            if num in higherDiff:
                result.add((higherDiff[num],num))
            
            lowerDiff[num-k] = num
            higherDiff[num+k] = num
                
        return len(result)
    