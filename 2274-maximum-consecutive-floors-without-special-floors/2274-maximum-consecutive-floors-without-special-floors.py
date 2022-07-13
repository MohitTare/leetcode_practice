class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        max_outside = max(special[0] -  bottom, top - special[-1])
        max_inside = 0
        for i in range(1,len(special)):
            max_inside = max(max_inside, special[i] -  special[i-1] - 1)
            
        return max(max_outside,max_inside)
        